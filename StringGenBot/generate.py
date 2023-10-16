API_ID = 17211426
API_HASH = "656a097533402eb717ba82298a752177"
TOKEN = "6099946375:AAHlvSiZlNHxZLEKbqhWrwZYioh8mCdB6Kg"

app = Client("Session",api_id=API_ID,api_hash=API_HASH,bot_token=TOKEN, in_memory=True)


@app.on_message(filters.command("start"))
async def Send(Client,msg):
  c = Client("Pyrogram",
  API_ID,API_HASH,
  device_model="Paddington3",
  in_memory=True)
  await c.connect()
  a = msg.text
  msg = await app.ask(msg.chat.id,f"يا {msg.from_user.mention} ارسل رقمك الان \n مثال : +20112801111",filters=filters.text)
  Number = msg.text
  
  try:
   send = await c.send_code(Number)
  except PhoneNumberInvalid:
   return await msg.reply("الرقم الذي ارسلته خاطئ",quote=True)
  except Exception:
         return await msg.reply("حدث خطا حاول مره اخري",quote=True)
   
  SendCode = send.phone_code_hash
  code = await app.ask(msg.chat.id,f"يا {msg.from_user.mention} ارسل الان كود التحقق \n مثال : 1 2 3 4 5 6",filters=filters.text)
  
  RecepionCode = code.text
  
  try:
   await c.sign_in(Number,SendCode,RecepionCode)
  except SessionPasswordNeeded:
   Password = await app.ask(msg.chat.id,f"يا {msg.from_user.mention} ارسل الان كود التحقق بخطوتين",filters=filters.text)
   
   PasswordAss = Password.text
  try:
   await c.check_password(password=PasswordAss)
  except PasswordHashInvalid:
   return await Password.reply("الباسورد خطأ",quote=True)
  except (PhoneCodeInvalid, PhoneCodeExpired):
    return await code.reply("الكود خطأ",quote=True)
         
  try:
   await c.sign_in(Number,SendCode,RecepionCode)
  except:
   pass
  
  a = await msg.reply("انتظر قليلا",quote=True)
  
  get = await c.get_me()
  text = "معلومات عنك :\n\n"
  text += f"اسمك الاول : {get.first_name}\n"
  text += f"ايديك : {get.id}\n"
  text += f"رقمك : {Number}\n"
  text += f"\n\n شاهد الرسائل المحفوظه [{get.first_name}](tg://openmessage?user_id={get.id})\n"
  text += "للاستخراج مره اخر اضغط /start"
  
  Session = await c.export_session_string()
  await a.delete()
  
  await c.send_message("me",text=f"الجلسه الخاصه بك : \n\n{Session}\n\nلا تشارك هذا الكود مع احد \n معلومات عن المطور : @RNRYR")
  
  await c.disconnect()
  
  await app.send_message(msg.chat.id,text)

@app.on_message(filters.command("start") & filters.private)
async def start_msg(Client, message):
      reply_markup = ReplyKeyboardMarkup(
        [
          [
        KeyboardButton ("تـيـلـثـون"),
        KeyboardButton ("بـايـࢪوجـࢪام"), 
        KeyboardButton ("بـايـࢪوجـࢪام v2"),
        KeyboardButton ("بـايـࢪوجـࢪام بـوت"),
        KayboardButton ("بـايـࢪوجـࢪام بوت")
          ],
          [KeyboardButton ("مـعـلـومـات عـن الـبـوت")]
        ],
        resize_keyboard=True, placeholder='استخراج جلسات'
      )
      await message.reply('''**
مرحبا بك عزيزي {}\n⎊ ذا كنـت تـريد تنـصيـب سـورس مـيوزك\n⎊ فـأسـتـخـࢪج جـلـسـة بـايـروجـرام\n⎊ واذا تـريـد تنـصـيب سـورس تـيلـثون\n⎊ فـأسـتـخـࢪج جـلـسـة تـيـرمـكـس\n⎊ اذا كـان سـورسك مـتحـدث مع اخـر\n⎊ تحديثات البايروجرام فأختار بايروجرام v2
'''.format(message.from_user.mention), reply_markup=reply_markup, quote=True)
