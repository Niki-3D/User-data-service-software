from src.repositories import UserRepository
from typing import Optional, List
from dataclasses import asdict


class UserController:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def create(self, user_data: dict) -> dict:
        user = self._repository.create(user_data)
        return asdict(user)

    def get_all(self) -> List[dict]:
        users = self._repository.get_all()
        return [asdict(user) for user in users]

    def get_by_id(self, user_id: int) -> Optional[dict]:
        user = self._repository.get_by_id(user_id)
        return asdict(user) if user else None

    def update(self, user_id: int, user_data: dict) -> Optional[dict]:
        user = self._repository.update(user_id, user_data)
        return asdict(user) if user else None

    def delete(self, user_id: int) -> bool:
        return self._repository.delete(user_id)
