import io
import re
import math
from . import catalive
from .. import CMD_LIST
from telethon import Button, custom, events

if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("Secret bot"):
            txt = re.findall(r'(\d+) ?(.*)', query[10:])
            text = txt[0][1]
            id = []
            id.append(txt[0][0])
            id.append(bot.uid)
            cat = (await bot.get_me()).id
            buttons = [custom.Button.inline("show message 🔐", data="secert")]
            result = builder.article(
                title="secret message",
                text=f"🔒 A whisper message to [user](tg://user?id={txt[0][0]}), Only he / she can open it.",
                buttons=buttons
            )
            await event.answer([result] if result else None)
            @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"secret")))
            async def on_plug_in_callback_query_handler(event):
                tcxt = text[10:]
                if event.query.user_id in id:
                    reply_pop_up_alert = tcxt
                    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
                else:
                    reply_pop_up_alert = "why were you looking at this shit go away and do your own work,idiot"
                    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)    
