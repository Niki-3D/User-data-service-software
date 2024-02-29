import pytest
from datetime import datetime
from src.repositories import UserRepository, User

@pytest.fixture()
def user_repository() -> UserRepository:
    return UserRepository()

def test_user_repository_exists() -> None:
    assert UserRepository

def test_create_user(user_repository: UserRepository) -> None:
    user_data = {
        "first_name": "John",
        "last_name": "Doe",
        "birth_year": 1990,
        "group": "user"
    }
    user_repository.create(user_data)
    actual = user_repository.get_all()
    assert actual == [User(1, "John", "Doe", 1990, "user")]
    

def test_get_all_users(user_repository: UserRepository) -> None:
    user_repository.create({
        "first_name": "John",
        "last_name": "Doe",
        "birth_year": 1990,
        "group": "user"
    })
    user_repository.create({
        "first_name": "Jane",
        "last_name": "Smith",
        "birth_year": 1985,
        "group": "premium"
    })
    actual = user_repository.get_all()
    assert actual == user_repository.users

def test_get_user_by_id(user_repository: UserRepository) -> None:
    user_repository.create({
        "first_name": "John",
        "last_name": "Doe",
        "birth_year": 1990,
        "group": "user"
    })
    actual = user_repository.get_by_id(1)
    assert actual == user_repository.users[0]


def test_update_user(user_repository: UserRepository) -> None:
    user = user_repository.create({
        "first_name": "John",
        "last_name": "Doe",
        "birth_year": 1990,
        "group": "user"
    })
    user_data = {
        "first_name": "Johnny",
        "last_name": "Doerson",
        "birth_year": 1985,
        "group": "premium"
    }
    actual = user_repository.update(user.id, user_data)
    assert actual.first_name == "Johnny"

def test_delete_user(user_repository: UserRepository) -> None:
    user = user_repository.create({
        "first_name": "John",
        "last_name": "Doe",
        "birth_year": 1990,
        "group": "user"
    })
    assert user_repository.delete(user.id) is True
