# app.py
from flask import Flask, render_template, request, jsonify, session
from .chatbot import chatbot_response
from . import config
import logging
from .storage import init_db, log_chat
from .ai_client import generate_ai_reply


# Initialize Flask app
app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = config.SECRET_KEY

# Configure Flask app
app.config['DEBUG'] = config.DEBUG
app.config['JSON_SORT_KEYS'] = False

# Configure logging
handlers = [logging.StreamHandler()]
if config.LOG_FILE:
    handlers.append(logging.FileHandler(config.LOG_FILE))
logging.basicConfig(level=getattr(logging, config.LOG_LEVEL, logging.INFO), handlers=handlers)
app.logger.setLevel(getattr(logging, config.LOG_LEVEL, logging.INFO))

init_db()


@app.route("/")
def home():
    """Serve the main chat interface."""
    return render_template("index.html")


@app.route("/get", methods=["GET"])
def get_bot_response():
    """
    Handle GET requests for chatbot responses.
    Expects 'msg' parameter in URL query string.
    """
    try:
        user_input = request.args.get("msg")
        
        if not user_input:
            return jsonify({
                "error": "No message provided",
                "message": "Please provide a 'msg' parameter"
            }), 400
        
        # Get response from chatbot
        # Maintain simple context in session
        session.setdefault('context', {})
        context = session['context']
        bot_response = chatbot_response(user_input.strip())
        # Store last message
        context['last_user_input'] = user_input.strip()
        session['context'] = context
        
        return jsonify({
            "response": bot_response,
            "status": "success"
        })
    
    except Exception as e:
        app.logger.error(f"Error in get_bot_response: {str(e)}")
        return jsonify({
            "error": "Internal server error",
            "message": "Something went wrong processing your request"
        }), 500


@app.route("/chat", methods=["POST"])
def chat():
    """
    Handle POST requests for chatbot responses.
    Accepts both JSON and form data.
    """
    try:
        user_msg = None
        
        # Handle JSON requests
        if request.is_json:
            data = request.get_json()
            if data:
                user_msg = data.get("message")
        
        # Handle form data requests
        elif request.form:
            user_msg = request.form.get("message")
        
        # Handle URL-encoded data
        elif request.data:
            try:
                import json
                data = json.loads(request.data.decode('utf-8'))
                user_msg = data.get("message")
            except (json.JSONDecodeError, UnicodeDecodeError):
                pass
        
        if not user_msg:
            return jsonify({
                "error": "No message provided",
                "message": "Please provide a 'message' field in your request"
            }), 400
        
        # Simple context memory
        session.setdefault('context', {})
        context = session['context']
        last_topic = context.get('last_topic')
        # Select mode
        mode = None
        if request.is_json and isinstance(data, dict):
            mode = data.get("mode")

        if mode == "ai":
            # Build short context from session chat history if needed
            history = session.get('ai_history', [])  # list of (role, content)
            # Add system primer
            system_prompt = (
                "You are FinTalkBot AI. Be concise, helpful, and accurate about finance topics."
            )
            messages = [("system", system_prompt)] + history + [("user", user_msg.strip())]
            bot_response = generate_ai_reply(messages)
            # Update history
            history.append(("user", user_msg.strip()))
            history.append(("assistant", bot_response))
            session['ai_history'] = history[-10:]  # keep last 10 turns
        else:
            bot_response = chatbot_response(user_msg.strip())
        # Update simple context
        context['last_user_input'] = user_msg.strip()
        # Naively infer last topic by extracting ticker-like tokens
        import re as _re
        found = _re.findall(r"\b[A-Za-z.-]{2,6}\b", user_msg)
        if found:
            context['last_topic'] = found[0].upper()
        elif any(name in user_msg.lower() for name in ['apple','tesla','bitcoin','ethereum']):
            context['last_topic'] = 'ALIAS'
        session['context'] = context
        
        reply_json = {
            "reply": bot_response,
            "status": "success",
            "user_input": user_msg
        }
        try:
            log_chat(user_msg.strip(), bot_response, mode)
        except Exception as _:
            pass
        return jsonify(reply_json)
    
    except Exception as e:
        app.logger.error(f"Error in chat endpoint: {str(e)}")
        return jsonify({
            "error": "Internal server error",
            "message": "Something went wrong processing your request"
        }), 500


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "service": "FinTalkBot API"
    })


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        "error": "Not found",
        "message": "The requested endpoint does not exist"
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 errors."""
    return jsonify({
        "error": "Method not allowed",
        "message": "The requested method is not allowed for this endpoint"
    }), 405


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({
        "error": "Internal server error",
        "message": "Something went wrong on our end"
    }), 500


# CORS support (if needed for frontend development)
@app.after_request
def after_request(response):
    """Add CORS headers to all responses."""
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


if __name__ == "__main__":
    # Run the Flask development server
    app.run(
        debug=config.DEBUG,
        host=config.HOST,
        port=config.PORT,
        threaded=True
    )