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

from typing import List, Optional

from UltronRoBo import LOGGER
from UltronRoBo.modules.users import get_user_id
from telegram import Message, MessageEntity
from telegram.error import BadRequest


def id_from_reply(message):
    prev_message = message.reply_to_message
    if not prev_message:
        return None, None
    user_id = prev_message.from_user.id
    res = message.text.split(None, 1)
    if len(res) < 2:
        return user_id, ""
    return user_id, res[1]


def extract_user(message: Message, args: List[str]) -> Optional[int]:
    return extract_user_and_text(message, args)[0]


def extract_user_and_text(
    message: Message, args: List[str]
) -> (Optional[int], Optional[str]):
    prev_message = message.reply_to_message
    split_text = message.text.split(None, 1)

    if len(split_text) < 2:
        return id_from_reply(message)  # only option possible

    text_to_parse = split_text[1]

    text = ""

    entities = list(message.parse_entities([MessageEntity.TEXT_MENTION]))
    ent = entities[0] if entities else None
    # if entity offset matches (command end/text start) then all good
    if entities and ent and ent.offset == len(message.text) - len(text_to_parse):
        ent = entities[0]
        user_id = ent.user.id
        text = message.text[ent.offset + ent.length :]

    elif len(args) >= 1 and args[0][0] == "@":
        user = args[0]
        user_id = get_user_id(user)
        if not user_id:
            message.reply_text(
                "𝑁𝑜 𝑖𝑑𝑒𝑎 𝑤ℎ𝑜 𝑡ℎ𝑖𝑠 𝑢𝑠𝑒𝑟 𝑖𝑠. 𝑌𝑜𝑢'𝑙𝑙 𝑏𝑒 𝑎𝑏𝑙𝑒 𝑡𝑜 𝑖𝑛𝑡𝑒𝑟𝑎𝑐𝑡 𝑤𝑖𝑡ℎ 𝑡ℎ𝑒𝑚 𝑖𝑓 "
                "𝑦𝑜𝑢 𝑟𝑒𝑝𝑙𝑦 𝑡𝑜 𝑡ℎ𝑎𝑡 𝑝𝑒𝑟𝑠𝑜𝑛'𝑠 𝑚𝑒𝑠𝑠𝑎𝑔𝑒 𝑖𝑛𝑠𝑡𝑒𝑎𝑑, 𝑜𝑟 𝑓𝑜𝑟𝑤𝑎𝑟𝑑 𝑜𝑛𝑒 𝑜𝑓 𝑡ℎ𝑎𝑡 𝑢𝑠𝑒𝑟'𝑠 𝑚𝑒𝑠𝑠𝑎𝑔𝑒𝑠."
            )
            return None, None

        else:
            user_id = user_id
            res = message.text.split(None, 2)
            if len(res) >= 3:
                text = res[2]

    elif len(args) >= 1 and args[0].isdigit():
        user_id = int(args[0])
        res = message.text.split(None, 2)
        if len(res) >= 3:
            text = res[2]

    elif prev_message:
        user_id, text = id_from_reply(message)

    else:
        return None, None

    try:
        message.bot.get_chat(user_id)
    except BadRequest as excp:
        if excp.message in ("User_id_invalid", "Chat not found"):
            message.reply_text(
                "𝐼 𝑑𝑜𝑛'𝑡 𝑠𝑒𝑒𝑚 𝑡𝑜 ℎ𝑎𝑣𝑒 𝑖𝑛𝑡𝑒𝑟𝑎𝑐𝑡𝑒𝑑 𝑤𝑖𝑡ℎ 𝑡ℎ𝑖𝑠 𝑢𝑠𝑒𝑟 𝑏𝑒𝑓𝑜𝑟𝑒 - 𝑝𝑙𝑒𝑎𝑠𝑒 𝑓𝑜𝑟𝑤𝑎𝑟𝑑 𝑎 𝑚𝑒𝑠𝑠𝑎𝑔𝑒 𝑓𝑟𝑜𝑚 "
                "𝑡ℎ𝑒𝑚 𝑡𝑜 𝑔𝑖𝑣𝑒 𝑚𝑒 𝑐𝑜𝑛𝑡𝑟𝑜𝑙! (𝑙𝑖𝑘𝑒 𝑎 𝑣𝑜𝑜𝑑𝑜𝑜 𝑑𝑜𝑙𝑙, 𝐼 𝑛𝑒𝑒𝑑 𝑎 𝑝𝑖𝑒𝑐𝑒 𝑜𝑓 𝑡ℎ𝑒𝑚 𝑡𝑜 𝑏𝑒 𝑎𝑏𝑙𝑒 "
                "𝑡𝑜 𝑒𝑥𝑒𝑐𝑢𝑡𝑒 𝑐𝑒𝑟𝑡𝑎𝑖𝑛 𝑐𝑜𝑚𝑚𝑎𝑛𝑑𝑠...)"
            )
        else:
            LOGGER.exception("Exception %s on user %s", excp.message, user_id)

        return None, None

    return user_id, text


def extract_text(message) -> str:
    return (
        message.text
        or message.caption
        or (message.sticker.emoji if message.sticker else None)
    )


def extract_unt_fedban(
    message: Message, args: List[str]
) -> (Optional[int], Optional[str]):
    prev_message = message.reply_to_message
    split_text = message.text.split(None, 1)

    if len(split_text) < 2:
        return id_from_reply(message)  # only option possible

    text_to_parse = split_text[1]

    text = ""

    entities = list(message.parse_entities([MessageEntity.TEXT_MENTION]))
    ent = entities[0] if entities else None
    # if entity offset matches (command end/text start) then all good
    if entities and ent and ent.offset == len(message.text) - len(text_to_parse):
        ent = entities[0]
        user_id = ent.user.id
        text = message.text[ent.offset + ent.length :]

    elif len(args) >= 1 and args[0][0] == "@":
        user = args[0]
        user_id = get_user_id(user)
        if not user_id and not isinstance(user_id, int):
            message.reply_text(
                "𝐼 𝑑𝑜𝑛'𝑡 ℎ𝑎𝑣𝑒 𝑡ℎ𝑎𝑡 𝑢𝑠𝑒𝑟 𝑖𝑛 𝑚𝑦 𝐷𝐵.  "
                "𝑌𝑜𝑢'𝑙𝑙 𝑏𝑒 𝑎𝑏𝑙𝑒 𝑡𝑜 𝑖𝑛𝑡𝑒𝑟𝑎𝑐𝑡 𝑤𝑖𝑡ℎ 𝑡ℎ𝑒𝑚 𝑖𝑓 𝑦𝑜𝑢 𝑟𝑒𝑝𝑙𝑦 𝑡𝑜 𝑡ℎ𝑎𝑡 𝑝𝑒𝑟𝑠𝑜𝑛'𝑠 𝑚𝑒𝑠𝑠𝑎𝑔𝑒 𝑖𝑛𝑠𝑡𝑒𝑎𝑑, 𝑜𝑟 𝑓𝑜𝑟𝑤𝑎𝑟𝑑 𝑜𝑛𝑒 𝑜𝑓 𝑡ℎ𝑎𝑡 𝑢𝑠𝑒𝑟'𝑠 𝑚𝑒𝑠𝑠𝑎𝑔𝑒𝑠."
            )
            return None, None

        else:
            user_id = user_id
            res = message.text.split(None, 2)
            if len(res) >= 3:
                text = res[2]

    elif len(args) >= 1 and args[0].isdigit():
        user_id = int(args[0])
        res = message.text.split(None, 2)
        if len(res) >= 3:
            text = res[2]

    elif prev_message:
        user_id, text = id_from_reply(message)

    else:
        return None, None

    try:
        message.bot.get_chat(user_id)
    except BadRequest as excp:
        if excp.message in ("User_id_invalid", "Chat not found") and not isinstance(
            user_id, int
        ):
            message.reply_text(
                "𝐼 𝑑𝑜𝑛'𝑡 𝑠𝑒𝑒𝑚 𝑡𝑜 ℎ𝑎𝑣𝑒 𝑖𝑛𝑡𝑒𝑟𝑎𝑐𝑡𝑒𝑑 𝑤𝑖𝑡ℎ 𝑡ℎ𝑖𝑠 𝑢𝑠𝑒𝑟 𝑏𝑒𝑓𝑜𝑟𝑒 "
                "- 𝑝𝑙𝑒𝑎𝑠𝑒 𝑓𝑜𝑟𝑤𝑎𝑟𝑑 𝑎 𝑚𝑒𝑠𝑠𝑎𝑔𝑒 𝑓𝑟𝑜𝑚 𝑡ℎ𝑒𝑚 𝑡𝑜 𝑔𝑖𝑣𝑒 𝑚𝑒 𝑐𝑜𝑛𝑡𝑟𝑜𝑙! "
                "(𝑙𝑖𝑘𝑒 𝑎 𝑣𝑜𝑜𝑑𝑜𝑜 𝑑𝑜𝑙𝑙, 𝐼 𝑛𝑒𝑒𝑑 𝑎 𝑝𝑖𝑒𝑐𝑒 𝑜𝑓 𝑡ℎ𝑒𝑚 𝑡𝑜 𝑏𝑒 𝑎𝑏𝑙𝑒 𝑡𝑜 𝑒𝑥𝑒𝑐𝑢𝑡𝑒 𝑐𝑒𝑟𝑡𝑎𝑖𝑛 𝑐𝑜𝑚𝑚𝑎𝑛𝑑𝑠...)"
            )
            return None, None
        elif excp.message != "Chat not found":
            LOGGER.exception("Exception %s on user %s", excp.message, user_id)
            return None, None
        elif not isinstance(user_id, int):
            return None, None

    return user_id, text


def extract_user_fban(message: Message, args: List[str]) -> Optional[int]:
    return extract_unt_fedban(message, args)[0]
