"""
VC Music Player, Telegram Voice Chat Userbot
Copyright (C) 2021  ZauteKm <https://telegram.dog/ZauteKm>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""
import os
import re
from youtube_dl import YoutubeDL
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM=os.environ.get("STREAM_URL", "https://youtu.be/21qNxnCS8WU")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM

class Config:
    ADMIN = os.environ.get("ADMINS", '1809714658')
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", '7333505'))
    CHAT = int(os.environ.get("CHAT", "-1001514622797"))
    LOG_GROUP=os.environ.get("LOG_GROUP", "-1001514622797")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "Y")
    ARQ_API=os.environ.get("ARQ_API", "IFBNMA-HNCLDF-BSSJIH-GKHIME-ARQ")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
    else:
        REPLY_MESSAGE=None
    EDIT_TITLE = os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE == "NO":
        EDIT_TITLE=None
    DURATION_LIMIT=int(os.environ.get("MAXIMUM_DURATION", 150))
    DELAY = int(os.environ.get("DELAY", 10))
    API_HASH = os.environ.get("API_HASH", "c75e455fa358cfa81920cd326110e5c6")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1913458765:AAGHuXQrCFzgsVZ3XM4msqVumbhQsfkB9tU") 
    SESSION = os.environ.get("SESSION_STRING", "BQBM471ILs4XLCK-lu3gtF7ga58GJrK8O1d1nzG9eeUL3kCq2EvDIqA0CKXqM-Vm87DFRiC_hMyg-h_dE4prFV2o0iTS2CoC5cWer2HTgPbApK95t1euCtQZzcDKSbsuP9m5cI99fzrJVbFGvlk6VKHMpyaxXS7bVvC93MgjsQHVyLvFxeWwhhqOzEhaR5Y_6vTBzW1hRrOKyGQWLsxJzgFg-mTbUoSdzAcn14oliczs7WRhBvcnObNHjb212CHhtlVbQqh_RVodeLG8lkbI82MvRQDFeOzCuGEzaGdO4p6N4QOYY2fFhAtgFL6JWdkBG8ulh25VEI9Vu58KaPhrTsmHa94N4gA")
    playlist=[]
    msg = {}
