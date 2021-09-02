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

from pyrogram import filters

from UltronRoBo.pyrogramee.pluginshelper import admins_only, get_text
from UltronRoBo import UltronRobo


@UltronRobo.on_message(filters.command("tagall") & ~filters.edited & ~filters.bot)
@admins_only
async def tagall(client, message):
    await message.reply("`Processing.....`")
    sh = get_text(message)
    if not sh:
        sh = "Hi!"
    mentions = ""
    async for member in client.iter_chat_members(message.chat.id):
        mentions += member.user.mention + " "
    n = 4096
    kk = [mentions[i : i + n] for i in range(0, len(mentions), n)]
    for i in kk:
        j = f"<b>{sh}</b> \n{i}"
        await client.send_message(message.chat.id, j, parse_mode="html")


@UltronRobo.on_message(filters.command("all") & ~filters.edited & ~filters.bot)
@admins_only
async def tagall(client, message):
    await message.reply("`Processing.....`")
    sh = get_text(message)
    if not sh:
        sh = "Hi!"
    mentions = ""
    async for member in client.iter_chat_members(message.chat.id):
        mentions += member.user.mention + " "
    n = 4096
    kk = [mentions[i : i + n] for i in range(0, len(mentions), n)]
    for i in kk:
        j = f"<b>{sh}</b> \n{i}"
        await client.send_message(message.chat.id, j, parse_mode="html")
        

__mod_name__ = "TagAll"
__help__ = """
- /tagall : Tag everyone in a chat
- /all : Tag everyone in a chat
"""
