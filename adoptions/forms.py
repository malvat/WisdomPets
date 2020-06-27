from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'submitter', 'species', 'breed', 'description', 'sex', 'submission_date', 'age', 'vaccination']
        widgets = {'vaccination': forms.CheckboxSelectMultiple, 'submission_date': forms.SelectDateWidget}