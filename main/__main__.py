import logging
import time
from main.server import server  # Import the server function from server.py
from cron import hit_server_url

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

botStartTime = time.time()

print("Successfully deployed!")
print("Bot Deployed : Saurav")

# Define a function to run the server URL hitting in a separate thread
def run_server_url():
    while True:
        hit_server_url()
        # Sleep for a specified duration before hitting the server URL again
        time.sleep(13 * 60)  # Sleep for 13 minutes

if __name__ == "__main__":
    from . import bot
    import threading
    import glob
    from pathlib import Path
    from main.utils import load_plugins
    
    # Start the server URL hitting function in a separate thread
    server_url_thread = threading.Thread(target=run_server_url)
    server_url_thread.start()

    # Start the server in a separate thread
    server_thread = threading.Thread(target=server)
    server_thread.start()

    # Load bot plugins
    path = "main/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            load_plugins(plugin_name.replace(".py", ""))
    
    # Start the bot
    logger.info("Bot Started :)")
    bot.run_until_disconnected()

    # Wait for the server thread to finish
    server_thread.join()
