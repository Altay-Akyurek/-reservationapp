
from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.user_login, name='user_login'),  # Burada 'name' parametresini ekledim
    path('kayıt', views.user_register,name='user_register'),
    path('rezervasyon_oluştur', views.create_reservation,name='create_reservation'),
    path('liste', views.user_register,name='reservation_list'),
    path('iptal', views.user_register,name='cancel_reservation'),
]