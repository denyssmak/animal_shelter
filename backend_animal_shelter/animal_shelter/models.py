from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.db import models


class MetaInfo(models.Model):  
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True


class TypeAnimal(MetaInfo):
    name = models.CharField(max_length=50, unique=True) 

    def __str__(self):
        return self.name


class Animal(MetaInfo):
    animal_type = models.ForeignKey(
        TypeAnimal, 
        on_delete=models.CASCADE, 
        related_name='animals',
    )

    name = models.CharField(max_length=50)
    date = models.DateField()
    
    height = models.PositiveIntegerField(
        
    )
    weight = models.DecimalField(
        decimal_places=3, 
        max_digits=7,
    )

    passport = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} | {self.date} | {self.height} | {self.weight}'

    @property
    def has_passport(self):
        return bool(getattr(self, 'passport'))

    @property  
    def years(self):
        return relativedelta(datetime.now(), self.date).years


class AnimalDeleteLog(MetaInfo):
    animal = models.OneToOneField(
        Animal, 
        on_delete=models.SET_NULL, 
        related_name='delete_log',
        null=True,
        blank=True,
    )
    reason = models.TextField()
    
    def __str__(self):
        return self.reason


class MedicalCard(MetaInfo):
    disease = models.TextField() 

    animal = models.ForeignKey(
        Animal, 
        on_delete=models.CASCADE, 
        related_name='animal_diseases',
    )
