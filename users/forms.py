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
        fields = ['username', 'email', 'password1', 'password2']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Continue'))
        
        # It just works
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-primary',
             onclick="window.location.href = '{}';".format(reverse('home'))))
        
        for i in self.fields.values():
            i.help_text = None
        

# LoginForm
class LoginForm(AuthenticationForm):
    class Meta:
        model = Lifter
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Login', css_class='btn-primary'))
        
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-primary',
             onclick="window.location.href = '{}';".format(reverse('home'))))
        
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Lifter
        fields = ['first_name', 'last_name', 'date_of_birth', 'height', 'weight', 'workouts_per_week']
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
                
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Changes'))
        
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-primary',
             onclick="window.location.href = '{}';".format(reverse('home'))))   
        
        # Sets every field as required
        for key in self.fields:
            self.fields[key].required = True