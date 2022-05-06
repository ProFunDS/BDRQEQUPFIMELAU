from config.tokens import MONGO_PASSWORD

from motor.motor_asyncio import AsyncIOMotorClient


db = AsyncIOMotorClient("cluster_address").database

users = db.users            # users collection
tg_keys = db.telegram_keys  # telegram keys collection
