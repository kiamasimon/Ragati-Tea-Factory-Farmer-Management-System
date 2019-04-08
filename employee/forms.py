from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from accounts.models import Sale, Employee


class AddSaleForm(ModelForm):

    class Meta:
        model = Sale
        fields = ('farmer_id', 'kg_of_tea', 'unit_cost', 'total', 'employee_id',)


class SignUpForm(UserCreationForm):

    class Meta:
        model = Employee
        fields = ('username', 'first_name', 'last_name', 'email', )