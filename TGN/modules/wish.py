import random
from PIL import Image
from TGN import telethn as neko
from telethon import events
@neko.on(events.NewMessage(pattern="/wish ?(.*)"))
async def wish(e):

 if e.is_reply:
         mm = random.randint(1,100)
         lol = await e.get_reply_message()
         fire = "https://telegra.ph/file/fd0d24d1d156f355572aa.jpg"
         await neko.send_file(e.chat_id, fire,caption=f"**Hey [{e.sender.first_name}](tg://user?id={e.sender.id}), Your wish has been cast.π**\n\n__chance of success {mm}%__", reply_to=lol)
 if not e.is_reply:
         mm = random.randint(1,100)
         fire = "https://telegra.ph/file/fd0d24d1d156f355572aa.jpg"
         await neko.send_file(e.chat_id, fire,caption=f"**Hey [{e.sender.first_name}](tg://user?id={e.sender.id}), Your wish has been cast.π**\n\n__chance of success {mm}%__", reply_to=e)




__help__ = """
Γ Κα΄Κα΄ wish α΄α΄α΄α΄Κα΄ use /wish and say anything 
 __if you need reading some hindi shayari so use__ /shayari __and see__Γ
"""

__mod_name__ = "wishπ«"

