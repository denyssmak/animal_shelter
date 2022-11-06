from django.contrib import admin

from animal_shelter.models import Animal, TypeAnimal


class AnimalAdmin(admin.ModelAdmin):
    fields = ('animal_type', 'name', 'date', 'height', 'weight', 'passport', )


admin.site.register(TypeAnimal)
admin.site.register(Animal, AnimalAdmin)
