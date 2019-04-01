from django.forms import ModelForm

from accounts.models import Sale


class AddSaleForm(ModelForm):

    class Meta:
        model = Sale
        fields = ('farmer_id', 'kg_of_tea', 'unit_cost', 'total','employee_id',)