from django.urls import path
from accounts import views

app_name = 'Accounts'
urlpatterns = [

    path('login', views.user_login, name='login'),
    path('signup', views.signup, name='signup'),
]