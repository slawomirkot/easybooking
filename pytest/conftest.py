import pytest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bookingvisit.models import *


@pytest.fixture
def user():
    u = User(username="Sławek")
    u.set_password('1234koT3')
    u.save()
    return u

@pytest.fixture
def client_profil(user):
    p = Client_Profil()
    p.user = user
    p.phone_number = '500600700'
    p.save()
    return p

@pytest.fixture
def authenticated_user(client):
    user = User(username="slaw231")
    user.set_password('1234koT54324fref6')
    user.save()
    client.login(username='slaw2311', password='1234koT54324fref6')
    return user

@pytest.fixture
def opinions1(user):
    o1 = Opinions.objects.create(rating='5', client_id='1', opinion="super", data='2021-07-03')
    return o1

