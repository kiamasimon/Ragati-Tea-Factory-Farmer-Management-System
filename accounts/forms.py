from django.contrib.auth.forms import UserCreationForm

from accounts.models import Farmer


class SignUpForm(UserCreationForm):

    class Meta:
        model = Farmer
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number','location')