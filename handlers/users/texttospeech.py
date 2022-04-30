import uuid
from gtts import gTTS
from loader import dp
from aiogram.types import Message



@dp.message_handler(content_types='text')
async def voice(msg: Message):
   language = 'ru'

   respond = gTTS(msg.text, lang=language, slow=False)
   voice_name = uuid.uuid4()
   respond.save(f"{voice_name}.wav")
   with open(f"{voice_name}.wav", 'rb') as f:
    await msg.reply_voice(f, caption=msg.text)

