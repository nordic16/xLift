from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Lifter

# Sign Up Form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = Lifter
        fields = ['username', 'email', 'password1', 'password2']
                
        help_texts = {
            'username' : None,
            'email' : None,
            'password confirmation' : None,
            'register' : None
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['email'].help_text = None
        self.fields['username'].help_text = None