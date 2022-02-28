from django import forms
from django.shortcuts import reverse
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField, AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions

from crispy_forms.layout import Submit, Button
from .models import Lifter


# Sign Up Form
class SignUpForm(UserCreationForm):
    class Meta:
        model = Lifter
        fields = ['username', 'email', 'password1', 'password2', 'weight', 'height', 'date_of_birth']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Sign Up'))
        
        # It just works
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-primary',
             onclick="window.location.href = '{}';".format(reverse('home'))))
        
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['email'].help_text = None
        self.fields['username'].help_text = None
        


# Sign Up Form
class LoginForm(AuthenticationForm):
    class Meta:
        model = Lifter
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Login'))
        
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-primary',
             onclick="window.location.href = '{}';".format(reverse('home'))))