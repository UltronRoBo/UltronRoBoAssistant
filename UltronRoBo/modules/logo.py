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

## 
@UltronLogo(pattern="^/blogo ?(.*)")
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
            fillcolor = "red"
            shadowcolor = "orange"
            font = ImageFont.truetype("./UltronRoBo/fonts/BeASt.ttf", 330)
            w, h = draw.textsize(text, font=font)
            h += int(h*0.21)
            image_width, image_height = img.size
            draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
            x = (image_widthz-w)/2
            y= ((image_heightz-h)/2+6)
            draw.text((x, y), text, font=font, fill="black", stroke_width=25, stroke_fill="red")
            fname2 = "LogoByUltronRoBo.png"
            img.save(fname2, "png")
            await tbot.send_file(event.chat_id, fname2, caption="**Logo created, and uploaded as per the request by 𝑼𝒍𝒕𝒓𝒐𝒏𝑹𝒐𝑩𝒐.**")
            if os.path.exists(fname2):
                os.remove(fname2)
                except Exception as e:
                    await event.reply(f'Error, Report at @UltronSupportChat, {e}')
                    

@UltronLogo(pattern="^/clogo ?(.*)")
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
            fillcolor = "blue"
            shadowcolor = "yellow"
            font = ImageFont.truetype("./UltronRoBo/fonts/CindrellaPersonalUse.ttf", 330)
            w, h = draw.textsize(text, font=font)
            h += int(h*0.21)
            image_width, image_height = img.size
            draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
            x = (image_widthz-w)/2
            y= ((image_heightz-h)/2+6)
            draw.text((x, y), text, font=font, fill="black", stroke_width=25, stroke_fill="blue")
            fname2 = "LogoByUltronRoBo.png"
            img.save(fname2, "png")
            await tbot.send_file(event.chat_id, fname2, caption="**Logo created, and uploaded as per the request by 𝑼𝒍𝒕𝒓𝒐𝒏𝑹𝒐𝑩𝒐.**")
            if os.path.exists(fname2):
                os.remove(fname2)
                except Exception as e:
                    await event.reply(f'Error, Report at @UltronSupportChat, {e}')
                    

@UltronLogo(pattern="^/crlogo ?(.*)")
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
            font = ImageFont.truetype("./UltronRoBo/fonts/Circus.ttf", 330)
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
                    

@UltronLogo(pattern="^/dclogo ?(.*)")
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
            font = ImageFont.truetype("./UltronRoBo/fonts/DeathCrow.ttf", 330)
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
                    

@UltronLogo(pattern="^/dslogo ?(.*)")
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
            font = ImageFont.truetype("./UltronRoBo/fonts/DroidSansMono.ttf", 330)
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
                    

@UltronLogo(pattern="^/flogo ?(.*)")
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
            font = ImageFont.truetype("./UltronRoBo/fonts/FlamanteStencilBold.ttf", 330)
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

                    
@UltronLogo(pattern="^/glogo ?(.*)")
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
            font = ImageFont.truetype("./UltronRoBo/fonts/GangOfThree.ttf", 330)
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
                    
                    
@UltronLogo(pattern="^/hlogo ?(.*)")
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
            font = ImageFont.truetype("./UltronRoBo/fonts/HanSolo.otf", 330)
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
                    
                    
@UltronLogo(pattern="^/ilogo ?(.*)")
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
            font = ImageFont.truetype("./UltronRoBo/fonts/Impact.ttf", 330)
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
                    
                    
@UltronLogo(pattern="^/lclogo ?(.*)")
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
            font = ImageFont.truetype("./UltronRoBo/fonts/LordcorpsStencil.ttf", 330)
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
                    
                    
@UltronLogo(pattern="^/lslogo ?(.*)")
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
            font = ImageFont.truetype("./UltronRoBo/fonts/LucidStreams.ttf", 330)
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
                    
                    
@UltronLogo(pattern="^/alogo ?(.*)")
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
            font = ImageFont.truetype("./UltronRoBo/fonts/LucidStreamsLaminar.ttf", 330)
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
                    
                    
@UltronLogo(pattern="^/nlogo ?(.*)")
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
            font = ImageFont.truetype("./UltronRoBo/fonts/NightMachine.ttf", 330)
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
                    
                    
@UltronLogo(pattern="^/qlogo ?(.*)")
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
            font = ImageFont.truetype("./UltronRoBo/fonts/Quivira.otf", 330)
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
                    
                    
@UltronLogo(pattern="^/rrlogo ?(.*)")
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
            font = ImageFont.truetype("./UltronRoBo/fonts/RoadRage.otf", 330)
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
                    
                    
@UltronLogo(pattern="^/rilogo ?(.*)")
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
            font = ImageFont.truetype("./UltronRoBo/fonts/Roboto-Italic.ttf", 330)
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
                    
                    
@UltronLogo(pattern="^/rmlogo ?(.*)")
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
            font = ImageFont.truetype("./UltronRoBo/fonts/Roboto-Medium.ttf", 330)
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
                    
                    
@UltronLogo(pattern="^/rlogo ?(.*)")
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
            font = ImageFont.truetype("./UltronRoBo/fonts/Robot-Regular.ttf", 330)
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
                    
                    
@UltronLogo(pattern="^/vlogo ?(.*)")
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
            font = ImageFont.truetype("./UltronRoBo/fonts/VampireWars.ttf", 330)
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
                    
                    
@UltronLogo(pattern="^/vilogo ?(.*)")
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
            font = ImageFont.truetype("./UltronRoBo/fonts/VampireWarsItalic.ttf", 330)
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
                    
                    
file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__mod_name__ = "Logo"
__help__ = """
 ❍ /logo <text>   *:* Logo with Chopsic Font.
 ❍ /wlogo <text>  *:* Logo with Maghrib Font.
 ❍ /blogo <text>  *:* Logo with BeASt Font.
 ❍ /clogo <text>  *:* Logo with CindrellaPersonalUse Font.
 ❍ /crlogo <text> *:* Logo with Circus Font.
 ❍ /dclogo <text> *:* Logo with DeathCrow Font.
 ❍ /dslogo <text> *:* Logo with DroidSansMono Font.
 ❍ /flogo <text>  *:* Logo with FlamanteStencilBold Font.
 ❍ /glogo <text>  *:* Logo with GangOfThree Font.
 ❍ /hlogo <text>  *:* Logo with HanSolo Font.
 ❍ /ilogo <text>  *:* Logo with Impact Font.
 ❍ /lclogo <text> *:* Logo with LordcorpsStencil Font.
 ❍ /lslogo <text> *:* Logo with LucidStreams Font.
 ❍ /alogo <text>  *:* Logo with LucidStreamsLaminar Font.
 ❍ /nlogo <text>  *:* Logo with NightMachine Font.
 ❍ /qlogo <text>  *:* Logo with Quivira Font.
 ❍ /rrlogo <text> *:* Logo with RoadRage Font.
 ❍ /rilogo <text> *:* Logo with Roboto-Italic Font.
 ❍ /rmlogo <text> *:* Logo with Roboto-Medium Font.
 ❍ /rlogo <text>  *:* Logo with Roboto-Regular Font.
 ❍ /vlogo <text>  *:* Logo with VampireWars Font.
 ❍ /vilogo <text> *:* Logo with VapireWarsItalic Font.
"""
