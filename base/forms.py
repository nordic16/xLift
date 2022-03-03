from users.models import Lifter
from django.forms import ModelForm    
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Submit, Button
from django.shortcuts import reverse


class ProfileForm(ModelForm):
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

    