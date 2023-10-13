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
        text=f"""مرحبا بك عزيزي {msg.from_user.mention}\n᭡︙ ذا كنـت تـريد تنـصيـب سـورس مـيوزك\n᭡︙ فـأسـتـخـࢪج جـلـسـة بـايـروجـرام\n᭡︙ واذا تـريـد تنـصـيب سـورس تـيلـثون\n᭡︙ فـأسـتـخـࢪج جـلـسـة تـيـرمـكـس\n᭡︙ اذا كـان سـورسك مـتحـدث مع اخـر\n᭡︙ تحديثات البايروجرام فأختار بايروجرام v2

᭡︙المـطور : [𝖺𝖧𝗆𝖤𝖽](tg://user?id=6373798952)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="⦓ بـدء اسـتـخـࢪاج جـلـسـة ⦔", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("Matrix arabic", url="https://t.me/Matrixthon"),
                    InlineKeyboardButton("aHmEd <\>", user_id=6373798952)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
