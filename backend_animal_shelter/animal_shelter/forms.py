from django import forms
from django.db.utils import OperationalError, ProgrammingError

from animal_shelter.models import Animal, TypeAnimal, AnimalDeleteLog, MedicalCard





class CreateUpdateAnimalDataForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('animal_type', 'name', 'date', 'height', 'weight', 'passport', )
        widgets = {
            'weight': forms.NumberInput(attrs={'step': 0.1, 'min': 0}),
            'passport': forms.TextInput(attrs={'pattern': '\\d*', 'maxlength': 7, 'minlength': 7}),
            'date': forms.DateInput(attrs={'type': 'date'})
        }
        

class CreateAnimalDataForm(CreateUpdateAnimalDataForm):
    pass


class UpdateAnimalDataForm(CreateUpdateAnimalDataForm):
    pass
        

class AnimalTypeFilterForm(forms.Form):
    animal_filter = forms.ModelChoiceField(TypeAnimal.objects.only('id', 'name'), empty_label='All', required=False)
    
        
class AnimalReasonForDeletionForm(forms.ModelForm):
    class Meta:
        model = AnimalDeleteLog
        fields = ('reason', )


class MedicalCardCreateDiseaseForm(forms.ModelForm):
    class Meta:
        model = MedicalCard
        fields = ('disease', )
