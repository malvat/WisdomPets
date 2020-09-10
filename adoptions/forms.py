from django import forms
from .models import Pet
from .models import User

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'submitter', 'species', 'breed', 'description', 'sex', 'submission_date', 'age', 'vaccination']
        widgets = {'vaccination': forms.CheckboxSelectMultiple, 'submission_date': forms.SelectDateWidget}

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }