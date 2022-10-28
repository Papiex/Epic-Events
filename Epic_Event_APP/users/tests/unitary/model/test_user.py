import pytest

from users.models import User


pytestmark = pytest.mark.django_db


@pytest.fixture
def create_user():
    user = User.objects.create(
        username = 'test',
        password = 'motdepasse78',
        first_name = 'test_first_name',
        last_name = 'test_last_name',
        email = 'test@test.test'
    )
    return user


class TestUserModel:

    def test_should_create_user(self, create_user):
        """test creating user"""
        user = create_user

        assert user.username == 'test'
        assert user.password == 'motdepasse78'
        assert user.first_name == 'test_first_name'
        assert user.last_name == 'test_last_name'
        assert user.email == 'test@test.test'


    def test_should_update_user(self, create_user):
        """test updating user"""
        user = create_user

        user.first_name = 'update_first_name'
        user.last_name = 'update_last_name'
        user.password = 'motdepasse79'
        user.email = 'test@newtest.test'
        user.username = 'test2'

        assert user.first_name == 'update_first_name'
        assert user.last_name == 'update_last_name'
        assert user.password == 'motdepasse79'
        assert user.email == 'test@newtest.test'
        assert user.username == 'test2'


    def test_should_get_user(self, create_user):
        """test get user"""
        user = create_user
        get_user = User.objects.all().first()

        assert user.username == get_user.username
        assert user.first_name == get_user.first_name
        assert user.last_name == get_user.last_name
        assert user.password == get_user.password
        assert user.email == get_user.email


    def test_should_delete_user(self, create_user):
        """test deleting user"""
        user = create_user
        user.delete()

        assert len(User.objects.all()) == 0