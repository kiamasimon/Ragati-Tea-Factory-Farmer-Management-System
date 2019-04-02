from django.urls import path, include

from farmer import views

app_name = 'Farmer'
urlpatterns = [
    path('index', views.index, name='index'),
    path('my_sales', views.individual_sales, name="my_sales")
]