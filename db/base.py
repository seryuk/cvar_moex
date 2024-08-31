import asyncio


from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from settings import settings
from db.db_config import metadata

engine = create_async_engine(
        url=settings.DB_DSN_ASYNC.get_secret_value(),
        echo=True,
)


SessionMaker = async_sessionmaker(engine)


if __name__ == '__main__':
    import db  # noqa


    async def create_db():
        async with engine.begin() as conn:
            await conn.run_sync(metadata.drop_all)
            await conn.run_sync(metadata.create_all)


    asyncio.run(create_db())
