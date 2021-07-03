import pytest
from django.test import Client, RequestFactory
from django.urls import reverse
from booking import urls
from bookingvisit import views
from django.contrib.auth.models import User




def test_anonymous(client):
    response = client.get('base.html')
    assert response.status_code == 200

def test_authenticat(client, django_user_model):
    username = "user1"
    first_name = "user"
    last_name = "last_user"
    email = "user1@o2.pl"
    password1 = "#%kdsakdDf234%"
    password2 = "#%kdsakdDf234%"
    username = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, password1=password1, password2=password2)
    client.login(username=username, password1=password1)
    response = Client.get('/')
    assert response.status_code == 200