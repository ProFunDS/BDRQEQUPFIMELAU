from datetime import datetime as dt

from aiogram.dispatcher import Dispatcher
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from config import GROUP_CHAT_ID
from config.rating_settings import EFL, PPM, WT

from telegram import bot
from telegram.decorators import check_direct

from mongo import users


async def on_message_event(msg: Message) -> None:
    if msg.chat.id != GROUP_CHAT_ID:
        return

    user = await users.find_one({'telegram_id': msg.from_user.id})
    if user is None:
        return

    now = dt.now()
    if (now - user['time']).seconds > WT:
        exp = user['exp'] + PPM
        await users.update_one({'telegram_id': msg.from_user.id},
            {'$set': {'exp': exp, 'time': now}})

@check_direct
async def my_statistics_command(msg: Message) -> None:
    user = msg.from_user
    
    user_entry = await users.find_one({'telegram_id': user.id})
    if user_entry is None:
        t = 'Please connect your telegram account to the our discord bot\n/my_secret_key'
        return await bot.send_message(user.id, t)

    level, exp = user_entry['exp']//EFL, user_entry['exp']%EFL

    t = f'''
    🔥  {hbold('PROJECT NAME')}\n
    {hbold('Experience')}
    Level: {hbold(str(level))} | {hbold(f'{exp}/{EFL}')} | {hbold(str(round(exp/EFL*100, 1)))}%
    
    {hbold('Discord referrals')}
    Score: {hbold(str(user_entry["im"]))}
    
    Discord referrer: {'✅' if user_entry['refer_id'] else '❌'}'''

    await bot.send_message(user.id, t) 

def register_extension(dp: Dispatcher) -> None:
    dp.register_message_handler(my_statistics_command,
                                commands=['my_statistics'])
    dp.register_message_handler(on_message_event)
