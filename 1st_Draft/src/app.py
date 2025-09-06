# app.py
from flask import Flask, render_template, request, jsonify
from src.chatbot import chatbot_response


# Initialize Flask app
app = Flask(__name__, template_folder="templates", static_folder="static")

# Configure Flask app
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False


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
        bot_response = chatbot_response(user_input.strip())
        
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
        
        # Get response from chatbot
        bot_response = chatbot_response(user_msg.strip())
        
        return jsonify({
            "reply": bot_response,
            "status": "success",
            "user_input": user_msg
        })
    
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
        debug=True,
        host="0.0.0.0",  # Allow external connections
        port=5000,
        threaded=True
    )