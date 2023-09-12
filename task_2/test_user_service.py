import asyncio
import unittest
from user_service import UserService
from models.database import async_session
from schemas.users import UserDTO


class TestUserService(unittest.TestCase):
    def setUp(self) -> None:
        self.user_service = UserService(async_session)

    def test_add(self):
        user_to_add = UserDTO(username="user", email="new_user@example.com")
        added_user = asyncio.run(self.user_service.add(user_to_add))
        asyncio.run(self.user_service.remove(added_user.id))

        self.assertEqual([added_user.username, added_user.email], ['user', 'new_user@example.com'])

    def test_get(self):
        user_to_add = UserDTO(username="user", email="new_user@example.com")
        added_user = asyncio.run(self.user_service.add(user_to_add))
        retrieved_user = asyncio.run(self.user_service.get(added_user.id))
        asyncio.run(self.user_service.remove(added_user.id))

        self.assertEqual([retrieved_user.username, retrieved_user.email], ['user', 'new_user@example.com'])

    def test_remove(self):
        user_to_add = UserDTO(username="user", email="new_user@example.com")
        added_user = asyncio.run(self.user_service.add(user_to_add))
        is_remove = asyncio.run(self.user_service.remove(added_user.id))

        self.assertEqual(is_remove, True)
