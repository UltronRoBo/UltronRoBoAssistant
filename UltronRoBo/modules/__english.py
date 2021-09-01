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

from UltronRoBo import telethn as tbot
import json
import os
os.system("pip installPyDictionary")
import requests
from UltronRoBo.events import register
from telethon import *
from telethon.tl import functions
import os
import urllib.request
from typing import List
from typing import Optional
from PyDictionary import PyDictionary
from telethon.tl import types
from telethon.tl.types import *


API_KEY = "6ae0c3a0-afdc-4532-a810-82ded0054236"
URL = "http://services.gingersoftware.com/Ginger/correct/json/GingerTheText"


@register(pattern="^/spell(?: |$)(.*)")
async def _(event):
    ctext = await event.get_reply_message()
    msg = ctext.text
    #  print (msg)
    params = dict(lang="US", clientVersion="2.0", apiKey=API_KEY, text=msg)

    res = requests.get(URL, params=params)
    changes = json.loads(res.text).get("LightGingerTheTextResult")
    curr_string = ""
    prev_end = 0

    for change in changes:
        start = change.get("From")
        end = change.get("To") + 1
        suggestions = change.get("Suggestions")
        if suggestions:
            sugg_str = suggestions[0].get("Text")
            curr_string += msg[prev_end:start] + sugg_str
            prev_end = end

    curr_string += msg[prev_end:]
    await event.reply(curr_string)


dictionary = PyDictionary()


@register(pattern="^/define")
async def _(event):
    text = event.text[len("/define ") :]
    word = f"{text}"
    let = dictionary.meaning(word)
    set = str(let)
    jet = set.replace("{", "")
    net = jet.replace("}", "")
    got = net.replace("'", "")
    await event.reply(got)


@register(pattern="^/synonyms")
async def _(event):
    text = event.text[len("/synonyms ") :]
    word = f"{text}"
    let = dictionary.synonym(word)
    set = str(let)
    jet = set.replace("{", "")
    net = jet.replace("}", "")
    got = net.replace("'", "")
    await event.reply(got)


@register(pattern="^/antonyms")
async def _(event):
    text = message.text[len("/antonyms ") :]
    word = f"{text}"
    let = dictionary.antonym(word)
    set = str(let)
    jet = set.replace("{", "")
    net = jet.replace("}", "")
    got = net.replace("'", "")
    await event.reply(got)



__help__ = """
• `/define` `<text>`*:* Type the word or expression you want to search\nFor example /define kill
• `/spell`*:* while replying to a message, will reply with a grammar corrected version
• `/synonyms` `<word>`*:* Find the synonyms of a word
• `/antonyms` `<word>`*:* Find the antonyms of a word
"""

__mod_name__= "English"
