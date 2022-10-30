from django import forms
from .models import Animal, TypeAnimal, AnimalDeleteLog, MedicalСard

ANIMALS_TYPE_CHOICES = [
    (animal_type.id, animal_type.name) 
    for animal_type in TypeAnimal.objects.only('id', 'name')
]


class CreateAnimalDataForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('animal_type', 'name', 'date', 'height', 'weight', 'passport', )
        widgets = {
            'weight': forms.NumberInput(attrs={'step': 0.1, 'min': 0}),
            'passport': forms.TextInput(attrs={'pattern':'\\d*', 'maxlength':7, 'minlength':7}),
            'date' : forms.DateInput(attrs={'type': 'date'})
        }


class UpdateAnimalDataForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('animal_type', 'name', 'date', 'height', 'weight', 'passport', )
        widgets = {
            'weight': forms.NumberInput(attrs={'step': 0.1, 'min': 0}),
            'passport': forms.TextInput(attrs={'pattern':'\\d*', 'maxlength':7, 'minlength':7}),
            'date' : forms.DateInput(attrs={'type': 'date'})
        }


class AnimalTypeFilterForm(forms.Form):
    animal_filter = forms.ChoiceField(choices=ANIMALS_TYPE_CHOICES)  # Rendering after start app


class AnimalReasonForDeletionForm(forms.ModelForm):
    class Meta:
        model = AnimalDeleteLog
        fields = ('reason', )


class MedicalСardCreateDiseaseForm(forms.ModelForm):
    class Meta:
        model = MedicalСard
        fields = ('disease', )
