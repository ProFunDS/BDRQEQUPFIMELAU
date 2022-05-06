from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from config.tokens import TELEGRAM_TOKEN


bot = Bot(token=TELEGRAM_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)
