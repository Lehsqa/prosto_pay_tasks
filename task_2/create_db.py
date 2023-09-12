import asyncio

from models.database import init_models
from models.users import User


asyncio.run(init_models())
