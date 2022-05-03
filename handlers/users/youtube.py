from aiogram import types

from loader import dp
from aiogram.dispatcher.filters import Text
from pytube import YouTube

@dp.message_handler(Text(startswith="https"))
async def get_audio(message:types.Message):
    link=message.text
    from io import BytesIO
    buffer=BytesIO()
    url=YouTube(link)
    if url.check_availability() is None:
        audio=url.streams.get_audio_only()
        audio.stream_to_buffer(buffer=buffer)
        buffer.seek(0)
        filename=url.title
        await message.answer_audio(audio=buffer,caption=filename,title=url.title,duration=url.length)
    else:
        await message.answer("Nimadir xato ketdi qayta tekshirib koring")
        