from pyrogram.types import Message
from telethon import TelegramClient
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, KeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from old_pyro.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

import config



ask_ques = "**⎊ ذا كنـت تـريد تنـصيـب سـورس مـيوزك\n⎊ فـأسـتـخـࢪج جـلـسـة بـايـروجـرام\n⎊ واذا تـريـد تنـصـيب سـورس تـيلـثون\n⎊ فـأسـتـخـࢪج جـلـسـة تـيـرمـكـس\n⎊ اذا كـان سـورسك مـتحـدث مع اخـر\n⎊ تحديثات البايروجرام فأختار بايروجرام v2\n⎊ يـوجـد اسـتـخـرج جـلسـات ل البـوتات :**"


buttons_ques = [
    [
        KeyboardButton("❬ بـايـࢪوجـࢪام ❭", callback_data="old_pyro"),
        KeyboardButton("❬ بـايـࢪوجـࢪام v2 ❭", callback_data="pyrogram"),
    ],
    [
        KeyboardButton("❬ تـيـلـثـون ❭", callback_data="telethon"),
    ],
    [
        KeyboardButton("❬ بـايـࢪوجـࢪام بـوت ❭", callback_data="pyrogram_bot"),
        KeyboardButton("❬ تـيـلـثـون بـوت ❭", callback_data="telethon_bot"),
    ],
]

gen_button = [
    [
        KeyboardButton(text="⦓ بـدء اسـتـخـࢪاج جـلـسـة ⦔", callback_data="generate")
    ]
]




@Client.on_message(filters.private & ~filters.forwarded & filters.command(["generate", "gen", "string", "str"]))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    if telethon:
        ty = "تـيلـثـون"
    else:
        ty = "بـايـࢪوجـࢪام"
        if not old_pyro:
            ty += " ᴠ2"
    if is_bot:
        ty += " بـوت"
    await msg.reply(f"⎊¦ بـدء إنـشـاء جـلسـة **{ty}** ...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, "⎊ اࢪسـل الان ايبي ايدي API_ID\n\n⎊ اضـغـط /skip لـلـتـخـطـي", filters=filters.text)
    if await cancelled(api_id_msg):
        return
    if api_id_msg.text == "/skip":
        api_id = config.API_ID
        api_hash = config.API_HASH
    else:
        try:
            api_id = int(api_id_msg.text)
        except ValueError:
            await api_id_msg.reply("⎊ يجب ان يكون ايبي ايدي عدداً صحيحاً \n⎊ يࢪجي المحـاولة مـࢪة أخـࢪى...", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
            return
        api_hash_msg = await bot.ask(user_id, "⎊ اࢪسـل الان ايبي هاش API_HASH", filters=filters.text)
        if await cancelled(api_hash_msg):
            return
        api_hash = api_hash_msg.text
    if not is_bot:
        t = "⎊ اࢪسـل الان ࢪقمك مع ࢪمـز دولتك\n⎊ مثـال : +201023456789"
    else:
        t = "⎊ اࢪسـل الان توكن بوتك BOT_TOKEN\n⎊ مثل : `5432198765:abcdanonymousterabaaplol`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("⎊ انتظر سوف نرسل كود لحسابك بالتليجرام...")
    else:
        await msg.reply("⎊ محاولة تسجيل الدخول عبࢪ توكن البوت...")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        await msg.reply("⎊ لا يتطابق ايبي ايدي و ايبي هاش ❌\n⎊ مع نظام تطبيقات تيليجࢪام 🌐\n⎊ يࢪجى المحاولة مـࢪة أخـࢪى...", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply("⎊ لا ينتمي ࢪقم الهاتف الذي أࢪسلتة ❌\n⎊ إلى اي حساب علي التيليجࢪام 🌐\n⎊ يرجى المحاولة مـࢪة أخـࢪى...", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "⎊ ارسل الان كود التحقق الذي تم ارسالة لك\n⎊ ارسل كود التحقق مثل: 1 2 3 4 5\n⎊ مع فراغ بين الارقام...", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply("⎊ تم انتهاء وقت انشاء الجلسه\n⎊ يرجى محاولة انشاء الجلسة من البداية.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await msg.reply("⎊ كود التحقق الذي ارسلته غير صحيح\n⎊ يرجى المحاولة مرة أخرى... ", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await msg.reply("⎊ انتهت صلاحية  كود التحقق الذي أرسلته\n⎊ يرجى المحاولة مرة أخرى... ", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                two_step_msg = await bot.ask(user_id, "⎊ يرجي إرسال كلمة مرور التحقق بخطوتين للمتابعة", filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply("» تم انتهاء وقت الجلسه 5 دقائق يرجى اعاده استخراج الجلسه من البدايه.", reply_markup=InlineKeyboardMarkup(gen_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
                await two_step_msg.reply("⎊ كلمة المرور التي أرسلتها غير صحيحة\n⎊ يرجى المحاولة مرة أخرى...", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**⎊ هذه هي جلسة {ty} الخاصة بك** \n\n`{string_session}` \n\n⎊\n⎊ يرجي عدم مشاركتها مع احد\n⎊♥"
    try:
        if not is_bot:
            await bot.send_message(msg.chat.id, text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass

async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("**» تم إلغـاء استخـراج الجلسـة !**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("**» تم ترسيت البوت بنجـاح ✅ !**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/skip" in msg.text:
        return False
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("**» تم التخطـي  !**", quote=True)
        return True
    else:
        return False
