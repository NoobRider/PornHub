"""
Time In Profile Pic.....
Command: `.autopp`

:::::Credit Time::::::
1) Coded By: @s_n_a_p_s
2) Ported By: @r4v4n4 (Legend)
3) End Game Help By: @spechide


#curse: who ever edits this credit section will goto hell
"""
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from uniborg.util import admin_cmd
import asyncio
import shutil

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

@borg.on(admin_cmd("autopp ?(.*)"))
async def autopic(event):
    downloaded_file_name = "./ravana/original_pic.png"
    downloader = SmartDL(Config.RAVANA_LEELA, downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    photo = "photo_pfp.png"
    while not downloader.isFinished():
        place_holder = None
    shutil.copy(downloaded_file_name, photo)
    while True:
        im = Image.open(photo)
        file_test = im.rotate(-5, expand=False).save(photo, "PNG")
        current_time = datetime.now().strftime("⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ \n ⚡USERBOT TIMEZONE⚡ \n  Time: %H:%M:%S \n  Date: %d.%m.%y \n⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡")
        photo_complete = "./ravana/photo_complete.png"
        shutil.copy(photo, photo_complete)
        img = Image.open(photo_complete)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((50, 250), current_time, font=fnt, fill=(255, 255, 255))
        img.save(photo_complete)
        file = await event.client.upload_file(photo_complete)  # pylint:disable=E0602
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo_complete)
            await asyncio.sleep(60)
        except:
            return
