from django.contrib.auth.models import User
from django.db import migrations
from django.utils import timezone


def generate_superuser(apps, schema_editor):
    superuser = User.objects.create_superuser(
        username="admin",
        password="admin",
        last_login=timezone.now(),
        is_superuser=True,
        is_staff=True
    )

    superuser.save()


class Migration(migrations.Migration):
    dependencies = [
        ('animal_shelter', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(generate_superuser, lambda x, y: None)
    ]
