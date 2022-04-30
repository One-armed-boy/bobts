from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','last_name','first_name','nickname','email','sex','phone']
