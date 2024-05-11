#GitHub: devgaganin

import math
import os
import time
import json
from main.plugins.helpers import TimeFormatter, humanbytes

#------
FINISHED_PROGRESS_STR = "🟢"
UN_FINISHED_PROGRESS_STR = "🔴"
DOWNLOAD_LOCATION = "/app"


async def progress_for_pyrogram(
    current,
    total,
    bot,
    ud_type,
    message,
    start
):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        status = f"{DOWNLOAD_LOCATION}/status.json"
        if os.path.exists(status):
            with open(status, 'r+') as f:
                statusMsg = json.load(f)
                if not statusMsg["running"]:
                    bot.stop_transmission()
        speed = current / diff
        elapsed_time = round(diff) * 1
        time_to_completion = round((total - current) / speed) * 1
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        # Determine appropriate units for size display
        current_size = humanbytes(current)
        total_size = humanbytes(total)

        # ASCII art progress bar
        progress_bar_length = 20
        completed_blocks = int(percentage / (100 / progress_bar_length))
        remaining_blocks = progress_bar_length - completed_blocks
        progress_bar = "█" * completed_blocks + "░" * remaining_blocks

        progress = f"**Progress:**\n```\n{progress_bar}\n```"

        tmp = progress + "**\n__Completed__:** {0} of {1}\n**__Speed__**: {2}/s\n**__Time__**: {3}\n".format(
            current_size,
            total_size,
            humanbytes(speed),
            estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            text = f"{ud_type}\n {tmp}"
            if message.text != text or message.caption != text:
                if not message.photo:
                    await message.edit_text(text=f"{ud_type}\n {tmp}")

                else:
                    await message.edit_caption(caption=f"{ud_type}\n {tmp}")
        except:
            pass

