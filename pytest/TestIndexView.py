import pytest
from django.test import Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from bookingvisit.models import Opinions


@pytest.mark.django_db
def test_salon_login_test_user(client):
    response = client.post("/salon-login/")
    assert response.status_code == 302  # sprwdzanie url do logowania administratora

@pytest.mark.django_db
def test_salon_login_test_admin(client, admin_user):
    response = client.get("/salon-login/")
    assert response.status_code == 302  # sprwdzanie url do logowania administratora

@pytest.mark.django_db
def test_login_test_user(client):
    response = client.post("/login/")
    assert response.status_code == 200  # sprwdzanie url login

@pytest.mark.django_db
def test_login_test_no_user_in_bd(client, user):
    my_user_test = {'username': 'Daria', 'password': '1267koT'}
    response = client.post("/login/", my_user_test)
    assert response.status_code == 200  # ponownie wyswietli login gdy zle dane

@pytest.mark.django_db
def test_login_test_user_1(client, user):
    my_user_test = {'username': 'Sławek', 'password': '1234koT3'}
    response = client.post("/login/", my_user_test)
    assert response.status_code == 302  # poprawne logowanie , przekierowanie

@pytest.mark.django_db
def test_logout_user_redirect(client, user):
    c = Client()
    response = c.get("/authorisathion/logout/")
    assert response.status_code == 302  # testowanie logout

@pytest.mark.django_db
def test_logout_redirect(client):
    response = client.post("/authorisathion/logout/")
    assert response.status_code == 302  # testowanie ulr logout

@pytest.mark.django_db
def test_positive_signup(client):
    new = {'username': 'Slawek123', 'first_name': 'Sławomir', 'last_name': 'Kot', 'email': 'abcd1234@gmail.com', 'password1': 'AW5njWScmcSvS7S', 'password2': 'AW5njWScmcSvS7S'}
    response = client.post("/signup/", new)
    assert response.status_code == 302  # poprawne dane użytkownika

@pytest.mark.django_db
def test_wrong_password_signup(client):
    new = {'username': 'Slawek123', 'first_name': 'Sławomir', 'last_name': 'Kot', 'email': 'abcd1234@gmail.com', 'password1': 'AW5njWScmcSvS7S', 'password2': 'AW5njWScmcSv'}
    response = client.post("/signup/", new)
    assert response.status_code == 200  # zle haslo

@pytest.mark.django_db
def test_wrong_email_signup(client):
    new = {'username': 'Slawek123', 'first_name': 'Sławomir', 'last_name': 'Kot', 'email': 'abcd1234gmail.com', 'password1': 'AW5njWScmcSvS7S', 'password2': 'AW5njWScmcSvS7S'}
    response = client.post("/signup/", new)
    assert response.status_code == 200  # niepoprawny email

@pytest.mark.django_db
def test_index_url(client):
    response = client.get('/')
    assert response.status_code == 200  # test url index

@pytest.mark.django_db
def test_login_url(client):
    response = client.get('/login/')
    assert response.status_code == 200  # test url login

@pytest.mark.django_db
def test_singup_url(client):
    response = client.get('/signup/')
    assert response.status_code == 200  # test url singup

@pytest.mark.django_db
def test_opinion_url(client):
    response = client.get('/opinion/')
    assert response.status_code == 200  # test url opinion

@pytest.mark.django_db
def test_profil_url(client, client_profil):
    response = client.get(f'/profil/{client_profil.pk}/')
    assert response.status_code == 200  # test url profil(uzytkownik zalogowany)

@pytest.mark.django_db
def test_reservation_url(client, client_profil):
    response = client.get(f'/profil/reservation/{client_profil.pk}/')
    assert response.status_code == 200  # test url lista rezerwacji(uzytkownik zalogowany)

@pytest.mark.django_db
def test_profil_url(client, client_profil):
    response = client.get(f'/profil/{client_profil.pk}/')
    assert response.status_code == 200   # test url profil gdy uzytkownik zalogowany

@pytest.mark.django_db
def test_visit_hairdresser(client, client_profil):
    response = client.get(f'/profil/reservation-hairdresser/{client_profil.pk}/')
    assert response.status_code == 200   # test url reservation hairdesser gdu zalogowany

@pytest.mark.django_db
def test_visit_hairdresser_logout(client):
    response = client.get('/profil/reservation-hairdresser/')
    assert response.status_code == 404   # test url gdy nie zalogowany

@pytest.mark.django_db
def test_visit_hairdresser(client, client_profil):
    response = client.get(f'/profil/reservation-hairdresser/{client_profil.pk}/')
    assert response.status_code == 200   # test url reservation hairdesser gdu zalogowany

@pytest.mark.django_db
def test_visit_beautician(client, client_profil):
    response = client.get(f'/profil/{client_profil.pk}/reservation-beautician/')
    assert response.status_code == 200   # test url reservation beautician gdu zalogowany

@pytest.mark.django_db
def test_profil_opinion(client, client_profil):
    response = client.get(f'/profil/opinion/{client_profil.pk}')
    assert response.status_code == 200   # test url opinie uzytkownika gdu zalogowany

@pytest.mark.django_db
def test_profil_opinion_update(client, client_profil):
    response = client.get(f'/profil/opinion/{client_profil.pk}/update/')
    assert response.status_code == 404   # test edycja opinie uzytkownika gdu zalogowany i brak opinii

@pytest.mark.django_db
def test_url_profil_opinion_create(client, client_profil):
    response = client.get(f'/profil/{client_profil.pk}/create-opinion/')
    assert response.status_code == 200   # test url tworzenie opinie uzytkownika gdu zalogowany

@pytest.mark.django_db
def test_profil_opinion_delete(client, client_profil):
    response = client.get(f'/profil/opinion/{client_profil.pk}/delete/')
    assert response.status_code == 404   # test url usuwanie opinie uzytkownika gdu zalogowany i brak opinii

