from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Lifter
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



# Sign Up Form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = Lifter
        fields = ['username', 'email', 'password1', 'password2']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Sign Up'))
        
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['email'].help_text = None
        self.fields['username'].help_text = None