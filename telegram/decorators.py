from telegram import bot

from aiogram.types import Message
from aiogram.utils.exceptions import CantInitiateConversation

def check_direct(func):
    async def wrapper(msg: Message):
        if msg.chat.id != msg.from_user.id:
            try:
                await bot.send_message(msg.from_user.id,
                    'Please use only this chat to call commands')
                await msg.delete()
            except CantInitiateConversation:
                await msg.reply(f'Please start the bot via direct message @link_to_this_bot')
                return
        return await func(msg)
    return wrapper
