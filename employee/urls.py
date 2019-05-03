from django.urls import path
from employee import views

app_name = 'Employee'
urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('farmers_list', views.list_farmers, name='list_farmers'),
    path('farmer/deactivate/<int:farmer_id>', views.deactivate_farmer, name='deactivate_farmer'),
    path('farmer/activate/<int:farmer_id>', views.activate_farmer, name='activate_farmer'),
    path('sales_list', views.sales_list, name="sales_list"),
    path('farmer_sales/<int:pk>', views.farmer_sales, name='farmer_sales'),
    path('add_sale', views.add_sale, name='add_sale'),
    path('sign_up', views.admin_signup, name='sign_up'),
    path('tea_prices', views.tea_prices, name='tea_prices'),
    path('add_tea_pricing', views.add_tea_pricing, name='add_tea_pricing'),
    path('edit/tea/pricing/<int:tea_type_id>', views.edit_tea_pricing, name='edit_tea_pricing'),
    path('profile', views.profile, name='profile'),
    path('edit_profile/<int:user_id>', views.edit_profile, name='edit_profile'),
    path('manage_employees', views.manage_employees, name='manage_employees'),
    path('add_employee', views.add_employee, name='add_employee'),
    path('de_activate/employee/<int:employee_id>', views.deactivate_employee, name='deactivate_employee'),
    path('activate/employee/<int:employee_id>', views.activate_employee, name='activate_employee')
]