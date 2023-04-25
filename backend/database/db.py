from backend.database import models


class Database:

    def __init__(self, session_maker):
        print("Created DB!")
        self.session_maker = session_maker

    async def create_instance(self, size) -> models.PhotoInfo:
        async with self.session_maker() as session:
            instance = models.PhotoInfo(size=size)
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            await session.close()
            return instance
