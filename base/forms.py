from users.models import Lifter
from .models import Workout
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Submit, Button
from django.shortcuts import reverse


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'notes', 'intensity']
        
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        
        # TODO: find a way to increase the padding between fields and inputs.
        self.helper.add_input(Submit('Submit', 'Start', css_class='btn_primary'))
        self.helper.add_input(Button('Submit', 'Discard', css_class='btn_primary',
            onclick="window.location.href = '{}';".format(reverse('workouts'))))
        
        self.fields['name'].required = True
        self.fields['intensity'].required = True