import logging
from flask import Flask
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def server():
    # Create a Flask app
    app = Flask(__name__)

    # Route for handling GET requests
    @app.route('/')
    def handle_get_request():
        # Log a message when a GET request is received
        logger.info("GET request received!")
        return "GET request received!"

    # Get the port from environment variables or use default 5000
    port = int(os.getenv("PORT", 5000))

    # Run the Flask app on specified port
    app.run(host="0.0.0.0" , port=port)
