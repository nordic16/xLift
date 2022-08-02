from users.models import Lifter
from .models import Workout
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Submit, Button
from django.urls import reverse_lazy
from base.utils import exercises


class AddExerciseForm(forms.Form):
    Exercises = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, 
        queryset=exercises, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        
        self.helper.add_input(Submit('add-exercise', 'Add Exercises', css_class='btn-primary'))
        

class WorkoutCreationForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'notes']
        
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        
        self.helper.add_input(Submit('Submit', 'Start', css_class='btn_primary'))
        self.helper.add_input(Button('Submit', 'Discard', css_class='btn_primary',
            onclick="window.location.href = '{}';".format(reverse_lazy('workouts'))))
        
        self.fields['name'].required = True