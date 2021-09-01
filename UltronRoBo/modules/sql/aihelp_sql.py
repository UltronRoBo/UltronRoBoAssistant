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

import threading

from UltronRoBo.modules.sql import BASE, SESSION
from sqlalchemy import Column, String


class aiChats(BASE):
    __tablename__ = "ai_chats"
    chat_id = Column(String(14), primary_key=True)
    ses_id = Column(String(70))
    expires = Column(String(15))

    def __init__(self, chat_id, ses_id, expires):
        self.chat_id = chat_id
        self.ses_id = ses_id
        self.expires = expires


aiChats.__table__.create(checkfirst=True)

INSERTION_LOCK = threading.RLock()


def is_chat(chat_id):
    try:
        chat = SESSION.query(aiChats).get(str(chat_id))
        if chat:
            return True
        return False
    finally:
        SESSION.close()


def set_ses(chat_id, ses_id, expires):
    with INSERTION_LOCK:
        autochat = SESSION.query(aiChats).get(str(chat_id))
        if not autochat:
            autochat = aiChats(str(chat_id), str(ses_id), str(expires))
        else:
            autochat.ses_id = str(ses_id)
            autochat.expires = str(expires)

        SESSION.add(autochat)
        SESSION.commit()


def get_ses(chat_id):
    autochat = SESSION.query(aiChats).get(str(chat_id))
    sesh = ""
    exp = ""
    if autochat:
        sesh = str(autochat.ses_id)
        exp = str(autochat.expires)

    SESSION.close()
    return sesh, exp


def rem_chat(chat_id):
    with INSERTION_LOCK:
        autochat = SESSION.query(aiChats).get(str(chat_id))
        if autochat:
            SESSION.delete(autochat)

        SESSION.commit()


def get_all_chats():
    try:
        return SESSION.query(aiChats.chat_id).all()
    finally:
        SESSION.close()
