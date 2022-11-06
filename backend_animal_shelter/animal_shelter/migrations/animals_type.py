from django.db import migrations


def type_animal(apps, schema_editor):
    TypeAnimal  = apps.get_model('animal_shelter', 'TypeAnimal')
    type_names = ['Dog','Cat','Pig','Sheep','Rabbit','Fish','Hamster']
    TypeAnimal.objects.bulk_create([TypeAnimal(name=name) for name in type_names]) 


class Migration(migrations.Migration):
    dependencies = [
        ('animal_shelter', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(type_animal, lambda x, y: None)
    ]