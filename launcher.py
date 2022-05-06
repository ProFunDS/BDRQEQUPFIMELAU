from aiogram.types import BotCommand
from aiogram.utils import executor

from extensions import discord_ext, help_ext, rating_ext

from telegram import dp


async def set_default_commands(dp) -> None:
    await dp.bot.set_my_commands([
        BotCommand('start', 'Run a bot'),
        BotCommand('help', 'Get help information'),
        BotCommand('my_statistics',
            'Get info about my profile [Only if the account is connected to the our discord bot]'),
        BotCommand('show_links', 'Get a list of project references'),
        BotCommand('my_secret_key',
            'Get a secret key to connect a telegram account to our bot in discord')
        ])

if __name__ == '__main__':
    discord_ext.register_extension(dp)
    help_ext.register_extension(dp)
    rating_ext.register_extension(dp)
    executor.start_polling(dp, skip_updates=True,
                        on_startup=set_default_commands)
