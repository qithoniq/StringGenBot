from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""᥀︙اهلا عزيزي︙᥀ {msg.from_user.mention},

᥀︙اهلا بك في بوت استخراج جلسات︙᥀
᥀︙بوت استخراج جلسة سيشن تيليثون تيرمكس - سيشن بايروجرام - سيشن تيليثون بوت - سيشن تيليثون بايروجرام

❲ 𝖬𝖠𝖣𝖤 𝖶𝖨𝖳𝖧 𝖡𝖸 ❳ ︙ [᭡︙مبرمج البوت︙᭡](tg://user?id={OWNER_ID}) """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="᭡︙بدء استخراج الجلسة︙᭡", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("᭡︙سورس ماتركس︙᭡", url="https://t.me/MaTriXThon"),
                    InlineKeyboardButton("᭡︙مبرمج البوت︙᭡", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
