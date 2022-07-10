from .. import worker
from telethon import events, Button

@worker.on(events.NewMessage(incoming=True, pattern="/ankit"))
async def repo(event):
    await event.reply("Info About Ankit",
                    buttons=[
                        [Button.url("Github", url="https://github.com/LEGEND-ANKIT")],
                        [Button.url("Replit", url="https://replit.com/@ANKIT-OS")]
                    ])
