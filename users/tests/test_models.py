import pytest
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from users.models import User

# Testa a criação de um usuário válido.
@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(email="martin@exemplo.com", username="martin", password="martin12345")
    assert user.email == "martin@exemplo.com"
    assert user.username == "martin"
    assert user.check_password("martin12345")

# Testa a criação de um usuário sem email.
@pytest.mark.django_db
def test_create_user_without_email():
    with pytest.raises(ValidationError):
        User.objects.create_user(email="", username="martin", password="martin12345")

# Testa a validação do campo email.
@pytest.mark.django_db
def test_user_requires_email():
    with pytest.raises(ValidationError):
        user = User.objects.create_user(email=None, username="martin", password="martin12345")
        user.full_clean()

# Testa a unicidade do campo email.
@pytest.mark.django_db
def test_email_unique():
    User.objects.create_user(email="martin@exemplo.com", username="martin", password="martin12345")
    with pytest.raises(IntegrityError):
        User.objects.create_user(email="martin@exemplo.com", username="martin", password="martin12345")

# Testa a definição correta do nome da tabela no banco de dados para o modelo User.
@pytest.mark.django_db
def test_user_meta_db_table():
    assert User._meta.db_table == 'users'