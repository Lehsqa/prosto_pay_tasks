import asyncio
import unittest
from unittest.mock import MagicMock

from user_service import UserService
from models.database import async_session
from models.users import User
from schemas.users import UserDTO
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession


class TestUserService(unittest.TestCase):
    def setUp(self):
        # Create a mock async session and user DTO for testing
        self.async_session = MagicMock(spec=AsyncSession)
        self.user_dto = UserDTO(id=1, username="test_user", email="test@example.com")

        # Create an instance of the UserService with the async session
        self.user_service = UserService(async_session)

    def test_get_existing_user(self):
        # Mock the async session's execute method to return an existing user
        self.async_session.return_value.execute.return_value.scalar_one_or_none.return_value = User(**self.user_dto.model_dump())

        # Test getting an existing user
        result = asyncio.run(self.user_service.get(1))
        self.assertEqual(result, self.user_dto)

    def test_get_nonexistent_user(self):
        # Mock the async session's execute method to raise a NoResultFound exception
        self.async_session.return_value.execute.return_value.scalar_one_or_none.side_effect = NoResultFound()

        # Test getting a nonexistent user
        result = asyncio.run(self.user_service.get(2))
        self.assertEqual(result, None)

    def test_add_user(self):
        # Mock the async session's add, flush, and commit methods
        self.async_session.return_value.add.return_value.flush.return_value = None
        self.async_session.return_value.commit.return_value = None

        # Test adding a user
        result = asyncio.run(self.user_service.add(self.user_dto))
        self.assertEqual(result, self.user_dto)

    def test_remove_existing_user(self):
        # Mock the async session's execute, delete, flush, and commit methods
        self.async_session.return_value.execute.return_value.scalar_one_or_none.return_value = User(**self.user_dto.model_dump())
        self.async_session.return_value.delete.return_value.flush.return_value = None
        self.async_session.return_value.commit.return_value = None

        # Test removing an existing user
        result = asyncio.run(self.user_service.remove(1))
        self.assertTrue(result)

    def test_remove_nonexistent_user(self):
        # Mock the async session's execute method to return None (user not found)
        self.async_session.return_value.execute.return_value.scalar_one_or_none.return_value = None

        # Test removing a nonexistent user
        with self.assertRaises(ValueError):
            asyncio.run(self.user_service.remove(1))
