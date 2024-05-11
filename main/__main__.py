# main_script.py

import logging
import time
from main.server import server  # Import the server function from server.py

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

botStartTime = time.time()

print("Successfully deployed!")
print("Bot Deployed : Team SPY")

if __name__ == "__main__":
    from . import bot
    import threading
    import glob
    from pathlib import Path
    from main.utils import load_plugins
    
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

