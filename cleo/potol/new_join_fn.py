import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import pyrogram


from cleo import (
    AUTH_CHANNEL
)


async def new_join_f(client, message):
    chat_type = message.chat.type
    #if chat_type != "private":
    #    await message.reply_text(f"Current CHAT ID: <code>{message.chat.id}</code>\n\n bot by @b4bypips")
        # leave chat
   #     await client.leave_chat(
    #        chat_id=message.chat.id,
     #       delete=True
      #  )
    # delete all other messages, except for AUTH_CHANNEL
   # await message.delete(revoke=True)

#

async def help_message_f(client, message):
    # await message.reply_text("no one gonna help you 🤣🤣🤣🤣", quote=True)
    #channel_id = str(AUTH_CHANNEL)[4:]
    #message_id = 99
    # display the /help
    
    await message.reply_text("""

<code>/ytdl</code> : This command should be used as reply to a supported link

<code>/pytdl</code> : This command will download videos from youtube playlist link and will upload to telegram.

<code>/ytdl gdrive</code> : This will download and upload to your cloud.

<code>/pytdl gdrive</code> : This download youtube playlist and upload to your cloud.

<code>/leech</code> : This command should be used as reply to a magnetic link, a torrent link, or a direct link. [this command will SPAM the chat and send the downloads a seperate files, if there is more than one file, in the specified torrent]

<code>/gleech</code> : This command should be used as reply to a magnetic link, a torrent link, or a direct link. And this will download the files from the given link or torrent and will upload to the cloud using rclone.

<code>/tleech</code> : This will mirror the telegram files to ur respective cloud cloud.

<code>/getsize</code> : This will give you total size of your destination folder in cloud.

You can add <code>archive</code> <code>unzip</code> <code>untar</code> <code>unrar</code> after default cmd. ie <b><code>/leech archive</code></b>

""", disable_web_page_preview=True)


async def rename_message_f(client, message):
    inline_keyboard = []
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            text="read this?",
            url="https://t.me/keralagram/698909"
        )
    ])
    reply_markup = pyrogram.InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text(
        "please use @renamebot",
        quote=True,
        reply_markup=reply_markup
    )
