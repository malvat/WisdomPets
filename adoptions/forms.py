from django import forms

class PetForm(forms.Form):
    SEX_CHOICES = [("M", "Male"), ("F", "Female")]
    name = forms.CharField(label = "name", max_length=100)
    submitter = forms.CharField(label = "submitter", max_length=100)
    species = forms.CharField(label = "species", max_length=30)
    breed = forms.CharField(label = "breed", max_length=30)