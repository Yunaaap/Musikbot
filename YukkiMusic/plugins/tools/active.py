from pyrogram import filters
from pyrogram.types import Message

from strings import get_command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.database.memorydatabase import (
    get_active_chats,
    get_active_video_chats,
)

# Commands
ACTIVEVC_COMMAND = get_command("ACTIVEVC_COMMAND")
ACTIVEVIDEO_COMMAND = get_command("ACTIVEVIDEO_COMMAND")


@app.on_message(filters.command(ACTIVEVC_COMMAND) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ....ᴘʟᴇᴀsᴇ ʜᴏʟᴅ ᴏɴ")
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ's")
    else:
        await mystic.edit_text(
            f"**ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ's:-**\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(ACTIVEVIDEO_COMMAND) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text("ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ....ᴘʟᴇᴀsᴇ ʜᴏʟᴅ ᴏɴ")
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ's")
    else:
        await mystic.edit_text(
            f"**ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ's:-**\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["ac"]) & SUDOERS)
async def vc(client, message: Message):
    ac_audio = str(len(await get_active_chats()))

    await message.reply_text(f"ᴀᴄᴛɪᴠᴇ ᴄʜᴀᴛs ɪɴғᴏ: {ac_audio}")


__MODULE__ = "Online"
__HELP__ = """<blockquote><b><u>Active Commands:</u>

/ac: Displays a list of active voice chats on the bot.
/activevoice: Displays a list of active voice chats and video calls on the bot.
/activevideo: Displays a list of active video calls on the bot.
/stats: Displays the bot's statistics. </b></blockquote>"""
