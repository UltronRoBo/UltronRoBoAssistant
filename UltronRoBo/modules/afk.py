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

import random, html

from UltronRoBo import dispatcher
from UltronRoBo.modules.disable import (
    DisableAbleCommandHandler,
    DisableAbleMessageHandler,
)
from UltronRoBo.modules.sql import afk_sql as sql
from UltronRoBo.modules.users import get_user_id
from telegram import MessageEntity, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, Filters, MessageHandler, run_async

AFK_GROUP = 7
AFK_REPLY_GROUP = 8

# AFK

@run_async
def afk(update: Update, context: CallbackContext):
    args = update.effective_message.text.split(None, 1)
    user = update.effective_user

    if not user:  # ignore channels
        return

    if user.id in [777000, 1837687523]:
        return

    notice = ""
    if len(args) >= 2:
        reason = args[1]
        if len(reason) > 100:
            reason = reason[:100]
            notice = "\nYour AFK Reason was shortened to 100 characters."
    else:
        reason = ""

    sql.set_afk(update.effective_user.id, reason)
    fname = update.effective_user.first_name
    try:
        update.effective_message.reply_text("{} is now away!{}".format(fname, notice))
    except BadRequest:
        pass


@run_async
def no_longer_afk(update: Update, context: CallbackContext):
    user = update.effective_user
    message = update.effective_message

    if not user:  # ignore channels
        return

    res = sql.rm_afk(user.id)
    if res:
        if message.new_chat_members:  # dont say msg
            return
        firstname = update.effective_user.first_name
        try:
            options = [
                "{} is here!",
                "{} is back!",
                "{} is now in the chat!",
                "{} is awake!",
                "{} is back online!",
                "{} is finally here!",
                "Welcome back! {}",
                "Where is {}?\nIn the chat!",
            ]
            chosen_option = random.choice(options)
            update.effective_message.reply_text(chosen_option.format(firstname))
        except:
            return


@run_async
def reply_afk(update: Update, context: CallbackContext):
    bot = context.bot
    message = update.effective_message
    userc = update.effective_user
    userc_id = userc.id
    if message.entities and message.parse_entities(
        [MessageEntity.TEXT_MENTION, MessageEntity.MENTION]
    ):
        entities = message.parse_entities(
            [MessageEntity.TEXT_MENTION, MessageEntity.MENTION]
        )

        chk_users = []
        for ent in entities:
            if ent.type == MessageEntity.TEXT_MENTION:
                user_id = ent.user.id
                fst_name = ent.user.first_name

                if user_id in chk_users:
                    return
                chk_users.append(user_id)

            if ent.type != MessageEntity.MENTION:
                return

            user_id = get_user_id(message.text[ent.offset : ent.offset + ent.length])
            if not user_id:
                # Should never happen, since for a user to become AFK they must have spoken. Maybe changed username?
                return

            if user_id in chk_users:
                return
            chk_users.append(user_id)

            try:
                chat = bot.get_chat(user_id)
            except BadRequest:
                print("Error: Could not fetch userid {} for AFK module".format(user_id))
                return
            fst_name = chat.first_name

            check_afk(update, context, user_id, fst_name, userc_id)

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        fst_name = message.reply_to_message.from_user.first_name
        check_afk(update, context, user_id, fst_name, userc_id)


def check_afk(update, context, user_id, fst_name, userc_id):
    if sql.is_afk(user_id):
        user = sql.check_afk_status(user_id)
        if int(userc_id) == int(user_id):
            return
        if not user.reason:
            res = "{} is AFK.".format(fst_name)
            update.effective_message.reply_text(res)
        else:
            res = "{} is AFK.\nReason: <code>{}</code>".format(
                html.escape(fst_name), html.escape(user.reason)
            )
            update.effective_message.reply_text(res, parse_mode="html")
            
# Studying

@run_async
def study(update: Update, context: CallbackContext):
    args = update.effective_message.text.split(None, 1)
    user = update.effective_user

    if not user:  # ignore channels
        return

    if user.id in [777000, 1837687523]:
        return

    notice = "\n\nLet him/her study, and u also go for studying, don't waste time here..."
    if len(args) >= 2:
        reason = args[1]
        if len(reason) > 1000:
            reason = reason[:1000]
            notice = "\n\nLet him/her study, and u also go for studying, don't waste time on TG..."
    else:
        ultron_name = update.effective_user.first_name
        reason = f"Hey U, Yes U !!\nU're prohibited to disturb **{ultron_name}**, cuz he/she is busy with studying."

    sql.set_afk(update.effective_user.id, reason)
    fname = update.effective_user.first_name
    try:
        update.effective_message.reply_text("{} is now going to study.".format(fname))
    except BadRequest:
        pass
    
@run_async
def no_longer_studying(update: Update, context: CallbackContext):
    user = update.effective_user
    message = update.effective_message

    if not user:  # ignore channels
        return

    res = sql.rm_afk(user.id)
    if res:
        if message.new_chat_members:  # dont say msg
            return
        firstname = update.effective_user.first_name
        try:
            options = [
                "{} has completed his/her studies!",
                "{} is back after completing studies!",
                "{} is online again!",
                "{} has done with his/her studies, and now can chat!",
                "{} has appeared in the chat again!",
                "{} is finally here!",
                "Welcome back! {}\nI'm happy that u don't waste time like others, and have studied for today..",
                "Where was {}?\nNowhere, He/she was studying, and now is online!",
            ]
            chosen_option = random.choice(options)
            update.effective_message.reply_text(chosen_option.format(firstname))
        except:
            return

@run_async
def reply_studying(update: Update, context: CallbackContext):
    bot = context.bot
    message = update.effective_message
    userc = update.effective_user
    userc_id = userc.id
    if message.entities and message.parse_entities(
        [MessageEntity.TEXT_MENTION, MessageEntity.MENTION]
    ):
        entities = message.parse_entities(
            [MessageEntity.TEXT_MENTION, MessageEntity.MENTION]
        )

        chk_users = []
        for ent in entities:
            if ent.type == MessageEntity.TEXT_MENTION:
                user_id = ent.user.id
                fst_name = ent.user.first_name

                if user_id in chk_users:
                    return
                chk_users.append(user_id)

            if ent.type != MessageEntity.MENTION:
                return

            user_id = get_user_id(message.text[ent.offset : ent.offset + ent.length])
            if not user_id:
                # Should never happen, since for a user to become AFK they must have spoken. Maybe changed username?
                return

            if user_id in chk_users:
                return
            chk_users.append(user_id)

            try:
                chat = bot.get_chat(user_id)
            except BadRequest:
                print("Error: Could not fetch userid {} for STUDY module".format(user_id))
                return
            fst_name = chat.first_name

            check_afk(update, context, user_id, fst_name, userc_id)

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        fst_name = message.reply_to_message.from_user.first_name
        check_studying(update, context, user_id, fst_name, userc_id)


def check_studying(update, context, user_id, fst_name, userc_id):
    if sql.is_afk(user_id):
        user = sql.check_afk_status(user_id)
        if int(userc_id) == int(user_id):
            return
        if not user.reason:
            res = "Hey U, Yes U !!\nU're prohibited to disturb <b>{}</b>, cuz he/she is busy with studying.".format(fst_name)
            update.effective_message.reply_text(res)
        else:
            res = "Hey U, Yes U !!\nU're prohibited to disturb <b>{}</b>, cuz he/she is busy with studying.\n\n<code>{}</code>".format(
                html.escape(fst_name), html.escape(user.reason)
            )
            update.effective_message.reply_text(res, parse_mode="html")
            
            
AFK_HANDLER = DisableAbleCommandHandler("afk", afk)
AFK_REGEX_HANDLER = DisableAbleMessageHandler(
    Filters.regex(r"^(?i)brb(.*)$"), afk, friendly="afk"
)
NO_AFK_HANDLER = MessageHandler(Filters.all & Filters.group, no_longer_afk)
AFK_REPLY_HANDLER = MessageHandler(Filters.all & Filters.group, reply_afk)

STUDY_HANDLER = DisableAbleCommandHandler("study", study)
STUDY_REGEX_HANDLER = DisableAbleMessageHandler(
    Filters.regex(r"^(?i)study(.*)$"), study, friendly="study"
)
NO_STUDY_HANDLER = MessageHandler(Filters.all & Filters.group, no_longer_studying)
STUDY_REPLY_HANDLER = MessageHandler(Filters.all & Filters.group, reply_studying)
  
dispatcher.add_handler(AFK_HANDLER, AFK_GROUP)
dispatcher.add_handler(AFK_REGEX_HANDLER, AFK_GROUP)
dispatcher.add_handler(NO_AFK_HANDLER, AFK_GROUP)
dispatcher.add_handler(AFK_REPLY_HANDLER, AFK_REPLY_GROUP)

dispatcher.add_handler(STUDY_HANDLER, STUDY_GROUP)
dispatcher.add_handler(STUDY_REGEX_HANDLER, STUDY_GROUP)
dispathcer.add_handler(NO_STUDY_HANDLER, STUDY_GROUP)
dispatcher.add_handler(STUDY_REPLY_HANDLER, STUDY_REPLY_GROUP)

__mod_name__ = "AFK"
__command_list__ = [
    "afk", 
    "study",
]
__handlers__ = [
    (AFK_HANDLER, AFK_GROUP),
    (AFK_REGEX_HANDLER, AFK_GROUP),
    (NO_AFK_HANDLER, AFK_GROUP),
    (AFK_REPLY_HANDLER, AFK_REPLY_GROUP),
    (STUDY_HANDLER, STUDY_GROUP),
    (STUDY_REGEX_HANDLER, STUDY_GROUP),
    (NO_STUDY_HANDLER, STUDY_GROUP),
    (STUDY_REPLY_HANDLER, STUDY_REPLY_GROUP),
]
