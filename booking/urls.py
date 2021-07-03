from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from bookingvisit import views


urlpatterns = [
    path("authorisathion/", include('django.contrib.auth.urls')),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('', views.IndexView.as_view(), name='index'),
    path('salon-login/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('profil/<int:pk>/', views.ClientProfilView.as_view(), name='profil'),
    path('update-name/<int:pk>/', views.UserNameUpdateView.as_view(), name='name_update'),
    path('update/<int:pk>/', views.UserEmailUpdateView.as_view(), name='email_update'),
    path('update/<int:pk>/phone', views.UpdateClientProfilView.as_view(), name='number_update'),
    path('profil/<int:pk>/reservation-hairdresser/', views.ReservationHairdersesrView.as_view(), name='client_reservation_hairdresser'),
    path('profil/<int:pk>/reservation-beautician/', views.ReservationBeauticianView.as_view(), name='client_reservation_beautician'),
    path('profil/reservation/<int:pk>/', views.ReservationListView.as_view(), name='client_reservation_list'),
    path('opinion/', views.OpinionsListView.as_view(), name='opinions'),
    path('profil/opinion/<int:pk>', views.ClientOpinionListView.as_view(), name='client_opinion'),
    path('profil/<int:pk>/create-opinion/', views.ClientOpinonView.as_view(), name='create_client_opinion'),
    path('profil/opinion/<int:pk>/update/', views.ClientOpinonUpdateView.as_view(), name='client_opinion_update'),
    path('profil/opinion/<int:pk>/delete/', views.ClientOpinonDeleteView.as_view(), name='client_opinion_delete'),


]
