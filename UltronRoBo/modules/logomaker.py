"""
MIT License

Copyright (c) 2021 UltronRoBo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from UltronRoBo.events import UltronLogo
from UltronRoBo import OWNER_ID
from UltronRoBo import telethn as tbot

import os 
from PIL import Image, ImageDraw, ImageFont
import random

@UltronLogo(pattern="^/logo ?(.*)")
async def lego(event):
    quew = event.pattern_match.group(1)
    if event.sender_id == OWNER_ID:
        pass
    else:
        if not quew:
            await event.reply('Provide Some Text To Draw!')
            return
        else:
            pass
        await event.reply('Creating your logo... waimt!')
        try:
            text = event.pattern_match.group(1)
            img = Image.open('./UltronRoBo/resources/LogoBG.png')
            draw = ImageDraw.Draw(img)
            image_widthz, image_heightz = img.size
            pointsize = 500
            fillcolor = "gold"
            shadowcolor = "blue"
            font = ImageFont.truetype("./UltronRoBo/fonts/Chopsic.otf", 330)
            w, h = draw.textsize(text, font=font)
            h += int(h*0.21)
            image_width, image_height = img.size
            draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
            x = (image_widthz-w)/2
            y= ((image_heightz-h)/2+6)
            draw.text((x, y), text, font=font, fill="black", stroke_width=25, stroke_fill="yellow")
            fname2 = "LogoByUltronRoBo.png"
            img.save(fname2, "png")
            await tbot.send_file(event.chat_id, fname2, caption="**Logo created, and uploaded as per the request by 𝑼𝒍𝒕𝒓𝒐𝒏𝑹𝒐𝑩𝒐.**")
            if os.path.exists(fname2):
                os.remove(fname2)
                except Exception as e:
                    await event.reply(f'Error, Report at @UltronSupportChat, {e}')


@UltronLogo(pattern="^/wlogo ?(.*)")
async def lego(event):
    quew = event.pattern_match.group(1)
    if event.sender_id == OWNER_ID:
        pass
    else:
        if not quew:
            await event.reply('Provide Some Text To Draw!')
            return
        else:
            pass
        await event.reply('Creating your logo...wait!')
        try:
            text = event.pattern_match.group(1)
            img = Image.open('./UltronRoBo/resources/LogoBG.png')
            draw = ImageDraw.Draw(img)
            image_widthz, image_heightz = img.size
            pointsize = 500
            fillcolor = "white"
            shadowcolor = "blue"
            font = ImageFont.truetype("./UltronRoBo/fonts/Maghrib.ttf", 1000)
            w, h = draw.textsize(text, font=font)
            h += int(h*0.21)
            image_width, image_height = img.size
            draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
            x = (image_widthz-w)/2
            y= ((image_heightz-h)/2+6)
            draw.text((x, y), text, font=font, fill="white", stroke_width=0, stroke_fill="white")
            fname2 = "LogoByUltronRoBo.png"
            img.save(fname2, "png")
            await tbot.send_file(event.chat_id, fname2, caption="**Logo created, and uploaded as per the request by 𝑼𝒍𝒕𝒓𝒐𝒏𝑹𝒐𝑩𝒐.**")
            if os.path.exists(fname2):
                os.remove(fname2)
                except Exception as e:
                    await event.reply(f'Error, Report at @UltronSupportChat, {e}')
                    
file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__mod_name__ = "Logo"
