from django.db import migrations


def type_animal(apps, schema_editor):
    TypeAnimal = apps.get_model('animal_shelter', 'TypeAnimal')
    TypeAnimal.objects.create(name='Dog')
    TypeAnimal.objects.create(name='Cat')
    TypeAnimal.objects.create(name='Pig')
    TypeAnimal.objects.create(name='Sheep')
    TypeAnimal.objects.create(name='Rabbit')
    TypeAnimal.objects.create(name='Fish')
    TypeAnimal.objects.create(name='Hamster')
    TypeAnimal.objects.create(name='Raccoon')
    

class Migration(migrations.Migration):
    dependencies = [
        ('animal_shelter', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(type_animal, lambda x, y: None)
    ]