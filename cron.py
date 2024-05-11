import requests
from dotenv import load_dotenv
import os
import time

# Load environment variables from .env file
load_dotenv()

# Function to hit the server URL
def hit_server_url():
    server_url = os.getenv("SERVER_URL")
    if server_url:
        try:
            response = requests.get(server_url)
            response.raise_for_status()
            print('Server URL hit successfully:', response.text)
        except requests.exceptions.RequestException as e:
            print('Error hitting server URL:', e)
    else:
        print("Server URL not found in .env file.")

# Continuous execution of the function
# while True:
#     hit_server_url()
#     # Sleep for a specified duration before hitting the server URL again
#     time.sleep(13 * 60)  # Sleep for 13 minutes
