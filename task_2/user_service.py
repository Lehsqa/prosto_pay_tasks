from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy import select
from models.users import User
from schemas.users import UserDTO


class UserService:
    '''
    (__init__)
    Implementation Choice: The UserService class takes an async_db_session argument in its constructor, which
    is presumably an async session maker.

    Argumentation: Dependency injection is a good practice, as it allows the class to work with different database
    sessions or configurations. This makes the class more testable and flexible, as it can be easily adapted to
    different database setups.

    (get)
    Implementation Choice: The get method fetches user data based on a user ID asynchronously and returns a UserDTO.

    Argumentation: This method follows a common pattern for retrieving data from a database. It uses SQLAlchemy's select
    and scalar_one_or_none to handle the query and result. If the user is found, it returns a UserDTO, which is a data
    transfer object representing the user. If not found, it raises a ValueError, which is a reasonable choice to
    indicate a non-existent user.

    (add)
    Implementation Choice: The add method adds a new user to the database asynchronously and returns a UserDTO
    representing the added user.

    Argumentation: This method creates a new User instance from a UserDTO and adds it to the database using the
    SQLAlchemy session. It then commits the transaction and returns the DTO of the newly added user. This approach
    ensures data integrity and handles potential exceptions during database operations.

    (remove)
    Implementation Choice: The remove method deletes a user from the database asynchronously and returns
    True upon success.

    Argumentation: This method uses SQLAlchemy's delete to remove a user based on their ID. If the user is found and
    successfully deleted, it returns True. If the user is not found, it raises a ValueError to indicate that the user
    doesn't exist. This behavior is in line with the expectations for a remove operation.
    '''
    def __init__(self, async_db_session: async_sessionmaker[AsyncSession]):
        self.async_session = async_db_session

    async def get(self, user_id: int) -> UserDTO:
        async with self.async_session() as session:
            async with session.begin():
                result = await session.execute(
                    select(User).filter(User.id == user_id)
                )
                user_db = result.scalar_one_or_none()

                if user_db:
                    return UserDTO.model_validate(user_db)

    async def add(self, user: UserDTO) -> UserDTO:
        user_db = User(**user.model_dump())

        async with self.async_session() as session:
            async with session.begin():
                session.add(user_db)
                await session.flush()
                await session.commit()

        return UserDTO.model_validate(user_db)

    async def remove(self, user_id: int) -> bool:
        async with self.async_session() as session:
            async with session.begin():
                user = await session.execute(
                    select(User).filter(User.id == user_id)
                )
                user_db = user.scalar_one_or_none()

                if user_db:
                    await session.delete(user_db)
                    await session.flush()
                    await session.commit()
                else:
                    raise ValueError(f"User with id {user_id} not found")

        return True
