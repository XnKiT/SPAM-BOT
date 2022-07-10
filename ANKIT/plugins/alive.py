from telethon import events
import os
from .. import worker
from ANKIT import BOT_USERS, BOT_USER, ALIVE_NAME
import asyncio
currentversion = "ONLY ONE"

ALIVE_NAME = str(ALIVE_NAME) if ALIVE_NAME else "©ANKIT™"
import os
anie786 = os.environ.get("PM_IMG", None)
if not anie786:
 anie786 = "https://telegra.ph/file/b002d63974bd05ea7a336.jpg"
pm_caption = "• ANKIT Sᴘᴀᴍᴍᴇʀ ɪs: Oɴʟɪɴᴇ\n\n"
pm_caption += "• Pʏᴛʜᴏɴ: 3.9.7 \n"
pm_caption += "• Dᴀᴛᴀʙᴀsᴇ Sᴛᴀᴛᴜs:  Fᴜɴᴄᴛɪᴏɴᴀʟ\n"
pm_caption += "• Cᴜʀʀᴇɴᴛ Bʀᴀɴᴄʜ : `ANKIT`\n"
pm_caption += f"• Wᴏʀᴋᴇʀ Oғ : {ALIVE_NAME} \n"
pm_caption += "• Hᴇʀᴏᴋᴜ Dᴀᴛᴀʙᴀsᴇ : AWS - ωοяκíиg ρяορєяℓγ\n\n"
pm_caption += "• Cᴏᴘʏʀɪɢʜᴛ ϐγ : (c)ANKIT KUMAR™\n\n"
pm_caption += "• Mᴀᴅᴇ ʙʏ : [(c)XNKIT™](https://github.com/LEGEND-ANKIT)"


@worker.on(events.NewMessage(incoming=True, pattern="^/alive"))
async def alive(event):
  if not str(event.sender_id) in BOT_USERS:
    return await event.reply("kid you have no control on me (sed)")
  await worker.send_file(event.chat_id, anie786, caption=pm_caption)
