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

import html
import random
import UltronRoBo.modules.tds_string as tds_string
from UltronRoBo import dispatcher
from telegram import ParseMode, Update, Bot
from UltronRoBo.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@run_async
def truth(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(tds_string.TRUTH))

@run_async
def dare(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(tds_string.DARE))


__mode_name__ = "Truth & Dare"
__help__ = """
- /truth : Asks u a question.
- /dare : Gives u a dare.
"""
__command_list__ = ["truth", "dare"]

TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)


dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
