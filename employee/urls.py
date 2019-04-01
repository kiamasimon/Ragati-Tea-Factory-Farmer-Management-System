from django.urls import path
from employee import views

app_name = 'Employee'
urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('farmers_list', views.list_farmers, name='list_farmers'),
    path('farmer/deactivate/<int:farmer_id>', views.deactivate_farmer, name='deactivate_farmer'),
    path('farmer/activate/<int:farmer_id>', views.activate_farmer, name='activate_farmer'),
    path('sales_list', views.sales_list, name="sales_list"),
    path('farmer_sales/<int:pk>', views.farmer_sales, name='farmer_sales')
]