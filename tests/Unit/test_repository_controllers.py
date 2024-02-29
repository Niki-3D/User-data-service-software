import pytest
from unittest.mock import Mock

from src.repositories import UserRepository
from src.repository_controllers import UserController
from src.repositories import User

@pytest.fixture
def repository_mock() -> Mock:
    repository = Mock(UserRepository)
    # Mocking repository methods to return instances of User
    repository.create.return_value = User(1, "John", "Doe", 1990, "user")
    repository.get_by_id.return_value = User(1, "John", "Doe", 1990, "user")
    repository.update.return_value = User(1, "Jane", "Doe", 1995, "user")
    return repository



@pytest.fixture
def controller_instance(repository_mock: Mock) -> UserController:
    return UserController(repository=repository_mock)

def test_controller_instance_creation(controller_instance: UserController) -> None:
    assert isinstance(controller_instance, UserController)

def test_create_method_raises_not_implemented_error(controller_instance: UserController,
                                                    repository_mock: Mock) -> None:
    repository_mock.create.side_effect = NotImplementedError
    with pytest.raises(NotImplementedError):
        controller_instance.create({})

def test_create_method_passes_user_data_to_repository(controller_instance: UserController,
                                                      repository_mock: Mock) -> None:
    user_data = {"id": 0, "firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}
    controller_instance.create(user_data)
    repository_mock.create.assert_called_with(user_data)

def test_get_all_method_raises_not_implemented_error(controller_instance: UserController,
                                                     repository_mock: Mock) -> None:
    repository_mock.get_all.side_effect = NotImplementedError
    with pytest.raises(NotImplementedError):
        controller_instance.get_all()

def test_get_by_id_method_raises_not_implemented_error(controller_instance: UserController,
                                                        repository_mock: Mock) -> None:
    repository_mock.get_by_id.side_effect = NotImplementedError
    with pytest.raises(NotImplementedError):
        controller_instance.get_by_id(1)

def test_get_by_id_method_passes_user_id_to_repository(controller_instance: UserController,
                                                       repository_mock: Mock) -> None:
    user_id = 1
    controller_instance.get_by_id(user_id)
    repository_mock.get_by_id.assert_called_once_with(user_id)

def test_update_method_raises_not_implemented_error(controller_instance: UserController,
                                                    repository_mock: Mock) -> None:
    repository_mock.update.side_effect = NotImplementedError
    with pytest.raises(NotImplementedError):
        controller_instance.update(1, {})

def test_update_method_passes_data_to_repository(controller_instance: UserController,
                                                 repository_mock: Mock) -> None:
    user_id = 1
    user_data = {"id": 1, "firstName": "Jane", "lastName": "Doe", "birthYear": 1995, "group": "user"}
    controller_instance.update(user_id, user_data)
    repository_mock.update.assert_called_once_with(user_id, user_data)

def test_delete_method_raises_not_implemented_error(controller_instance: UserController,
                                                     repository_mock: Mock) -> None:
    repository_mock.delete.side_effect = NotImplementedError
    with pytest.raises(NotImplementedError):
        controller_instance.delete(1)

def test_delete_method_passes_user_id_to_repository(controller_instance: UserController,
                                                    repository_mock: Mock) -> None:
    user_id = 1
    controller_instance.delete(user_id)
    repository_mock.delete.assert_called_once_with(user_id)
