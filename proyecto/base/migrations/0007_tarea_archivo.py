# Generated by Django 5.1.2 on 2024-11-01 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_editartareas'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='archivos/'),
        ),
    ]