from django.contrib.auth.forms import UserCreationForm

from account.models import User

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("name", "email", "password1", "password2")