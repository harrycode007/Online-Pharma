# Generated by Django 2.2.1 on 2019-12-08 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0006_medicineordered_emaill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicineordered',
            name='emaill',
        ),
    ]
