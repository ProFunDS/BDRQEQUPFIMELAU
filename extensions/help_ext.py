from aiogram.dispatcher import Dispatcher
from aiogram.types import Message
from aiogram.utils.markdown import hbold, hlink

from telegram import bot
from telegram.decorators import check_direct


@check_direct
async def start_command(msg: Message) -> None:
    await bot.send_message(msg.from_user.id, 'Hello!')

@check_direct
async def help_command(msg: Message) -> None:
    await bot.send_message(msg.from_user.id, "It's empty at the moment :C")

show_links_text = f'''📌 {hbold('Our official links')}:
    {hlink('► Telegram Group', 'https://t.me/link')}
    {hlink('► Telegram Channel', 'https://t.me/link_2')}
    {hlink('► Discord', 'https://discord.gg/0000000000')}
    {hlink('► Twitter', 'https://twitter.com/link')}
    {hlink('► Medium', 'https://medium.com/link')}
    {hlink('► Youtube', 'https://youtube.com/link')}
    {hlink('► Twitch', 'https://www.twitch.tv/link')}'''

@check_direct
async def show_links_command(msg: Message) -> None:
    await bot.send_message(msg.from_user.id, show_links_text,
        disable_web_page_preview=True)

def register_extension(dp: Dispatcher) -> None:
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(show_links_command, commands=['show_links'])
