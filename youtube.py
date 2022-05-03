from aiogram import types

from loader import dp
from aiogram.dispatcher.filters import Text
from pytube import YouTube

@dp.messege_handler(Text(startswith="http"))
async def get_audio(message: types.message):
    link = message.text
    from io import BytesIO
    buffer = BytesIO()
    url=YouTube(link)
    if url.check_aviablity() is None:
        audio=url.streams.get_audio_only()
        audio.stream_to_buffer(buffer=buffer)
        buffer.deek(0)
        filename=url.title
        await message.answer_audio(audio=buffer,caption=filename)
    else:
        await message.answer('')