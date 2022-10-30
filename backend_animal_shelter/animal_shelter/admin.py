from django.contrib import admin


from .models import Animal, TypeAnimal, MedicalСard


class AnimalAdmin(admin.ModelAdmin):
    fields = ('animal_type', 'name', 'date', 'height', 'weight', 'passport', )

admin.site.register(TypeAnimal)
admin.site.register(MedicalСard)
admin.site.register(Animal, AnimalAdmin)

