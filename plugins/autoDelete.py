# +++ Made By Sanjiii [telegram username: @Urr_Sanjiii] +++

#from bot import Bot
import asyncio
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from datetime import datetime, timedelta

#Time conversion for auto delete timer
def convert_time(duration_seconds: int) -> str:
    periods = [
        ('ʏᴇᴀʀ', 60 * 60 * 24 * 365),
        ('ᴍᴏɴᴛʜ', 60 * 60 * 24 * 30),
        ('ᴅᴀʏ', 60 * 60 * 24),
        ('ʜᴏᴜʀ', 60 * 60),
        ('ᴍɪɴᴜᴛᴇ', 60),
        ('sᴇᴄᴏɴᴅ', 1)
    ]

    parts = []
    for period_name, period_seconds in periods:
        if duration_seconds >= period_seconds:
            num_periods = duration_seconds // period_seconds
            duration_seconds %= period_seconds
            parts.append(f"{num_periods} {period_name}{'s' if num_periods > 1 else ''}")

    if len(parts) == 0:
        return "0 sᴇᴄᴏɴᴅ"
    elif len(parts) == 1:
        return parts[0]
    else:
        return ', '.join(parts[:-1]) +' ᴀɴᴅ '+ parts[-1]


#=====================================================================================##
#.........Auto Delete Functions.......#
#=====================================================================================##
DEL_MSG = """<b>‼️ ᴅᴜᴇ ᴛᴏ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs ‼️
<blockquote>ʏᴏᴜʀ ғɪʟᴇs ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ᴡɪᴛʜɪɴ <a href="https://t.me/{username}">{time}</a>. sᴏ ᴘʟᴇᴀsᴇ ғᴏʀᴡᴀʀᴅ ᴛʜᴇᴍ ᴛᴏ sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇs ғᴏʀ ғᴜᴛᴜʀᴇ ᴀᴠᴀɪʟᴀʙɪʟɪᴛʏ.</blockquote></b>"""

#Function for provide auto delete notification message
async def auto_del_notification(bot_username, msg, delay_time, transfer): 
    temp = await msg.reply_text(DEL_MSG.format(username=bot_username, time=convert_time(delay_time)), disable_web_page_preview = True) 

    await asyncio.sleep(delay_time)
    try:
        if transfer:
            try:
                name = "‼️ ɴᴏᴡ ᴄʟɪᴄᴋ ʜᴇʀᴇ ‼️"
                link = f"https://t.me/{bot_username}?start={transfer}"
                button = [[InlineKeyboardButton(text=name, url=link), InlineKeyboardButton(text="• ᴄʟᴏsᴇ •", callback_data = "close")]]

                await temp.edit_text(text=f"<b>›› ᴘʀᴇᴠɪᴏᴜs ᴍᴇssᴀɢᴇ ᴡᴀs ᴅᴇʟᴇᴛᴇᴅ.\nɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇs ᴀɢᴀɪɴ, ᴛʜᴇɴ ᴄʟɪᴄᴋ: [<a href={link}>{name}</a>] ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴇʟsᴇ ᴄʟᴏsᴇ ᴛʜɪs ᴍᴇssᴀɢᴇ.</b>", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)

            except Exception as e:
                await temp.edit_text(f"<b><blockquote>›› ᴘʀᴇᴠɪᴏᴜs ᴍᴇssᴀɢᴇ ᴡᴀs ᴅᴇʟᴇᴛᴇᴅ 🗑</blockquote></b>")
                print(f"Error occured while editing the Delete message: {e}")
        else:
            await temp.edit_text(f"<b><blockquote>›› ᴘʀᴇᴠɪᴏᴜs ᴍᴇssᴀɢᴇ ᴡᴀs ᴅᴇʟᴇᴛᴇᴅ 🗑</blockquote></b>")

    except Exception as e:
        print(f"Error occured while editing the Delete message: {e}")
        await temp.edit_text(f"<b><blockquote>›› ᴘʀᴇᴠɪᴏᴜs ᴍᴇssᴀɢᴇ ᴡᴀs ᴅᴇʟᴇᴛᴇᴅ 🗑</blockquote></b>")

    try: await msg.delete()
    except Exception as e: print(f"Error occurred on auto_del_notification() : {e}")


#Function for deleteing files/Messages.....
async def delete_message(msg, delay_time): 
    await asyncio.sleep(delay_time)
    
    try: await msg.delete()
    except Exception as e: print(f"Error occurred on delete_message() : {e}")
    
    
# +++ Made By Sanjiii [telegram username: @Urr_Sanjiii] +++