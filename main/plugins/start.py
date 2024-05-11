import os
from .. import bot as saurav
from telethon import events, Button
from telethon.tl.types import InputMediaPhoto

S = "/start"
START_PIC = "https://res.cloudinary.com/drvntsbpo/image/upload/v1706031295/Golgappa-4_y3qpfs.jpg"
TEXT = "Send me the Link of any message of Restricted Channels to Clone it here.\nFor private channel's messages, send the Invite Link first.\n\n👉🏻Execute /batch for bulk process upto 10K files range."

def is_set_button(data):
    return data == "set"

def is_rem_button(data):
    return data == "rem"

@saurav.on(events.CallbackQuery(pattern=b"set"))
async def sett(event):    
    saurav = event.client
    button = await event.get_message()
    msg = await button.get_reply_message()
    await event.delete()
    async with saurav.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
            return
        mime = x.file.mime_type
        if 'png' not in mime and 'jpg' not in mime and 'jpeg' not in mime:
            return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Temporary thumbnail saved!")

@saurav.on(events.CallbackQuery(pattern=b"rem"))
async def remt(event):  
    saurav = event.client            
    await event.edit('Trying... to save Bamby ... Wait')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Removed!')
    except Exception:
        await event.edit("No thumbnail saved.")                        

@saurav.on(events.NewMessage(pattern=f"^{S}"))
async def start_command(event):
    # Creating inline keyboard with buttons
    buttons = [
        [Button.inline("SET THUMB", data="set"),
         Button.inline("REM THUMB", data="rem")],
        [Button.url("Join Channel", url="https://telegram.dog/aboutsaurav")]
    ]

    # Sending photo with caption and buttons
    await saurav.send_file(
        event.chat_id,
        file=START_PIC,
        caption=TEXT,
        buttons=buttons
    )

