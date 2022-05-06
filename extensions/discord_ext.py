from random import choice

from aiogram.dispatcher import Dispatcher
from aiogram.types import Message
from aiogram.utils.markdown import hbold, hlink

from telegram import bot
from telegram.decorators import check_direct

from mongo import tg_keys


@check_direct
async def secret_key_command(msg: Message) -> None: 
    user = msg.from_user   
    key_entry = await tg_keys.find_one({'_id': user.id})

    if key_entry:
        return await bot.send_message(
            user.id, f'Your secret key: {hbold(key_entry["key"])}')

    key = str(user.id).replace('', '*')
    for _ in range(key.count('*')):
        key = key.replace('*', choice('?!'), 1)

    await tg_keys.insert_one({'_id': user.id, 'key': key})

    t = f'''Now I will generate a secret key that you need to copy and paste in\
        the {hlink('discord', 'https://discord.gg/jyFFzGbghe')} channel using\
        the {hbold('/connect_telegram_account')} command.
    \nAfter connecting your account, your secret key will be deleted.
    \nPreferably write something in chats before using the command (e.g. 'hi' ).
    \nYour secret_key: {hbold(key)}'''
    await bot.send_message(user.id, t, disable_web_page_preview=True)

@check_direct
async def connect_telegram_account_command(msg: Message) -> None:
    await bot.send_message(msg.from_user.id,
        'This command is only for discord bot.\n/show_links')

def register_extension(dp: Dispatcher) -> None:
    dp.register_message_handler(secret_key_command,
                                commands=['my_secret_key'])
    dp.register_message_handler(connect_telegram_account_command,
                                commands=['connect_telegram_account'])
