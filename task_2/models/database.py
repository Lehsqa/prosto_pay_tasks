from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_NAME = 'app.sqlite'

engine = create_async_engine(f'sqlite+aiosqlite:///{DATABASE_NAME}')
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)

Base = declarative_base()


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
