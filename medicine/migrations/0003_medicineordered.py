# Generated by Django 2.2.1 on 2019-12-08 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicineOrdered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Combiflam', models.IntegerField(default=0)),
                ('Paracetamol', models.IntegerField(default=0)),
                ('Cofsils', models.IntegerField(default=0)),
                ('DigeneTablet', models.IntegerField(default=0)),
                ('DigeneGel', models.IntegerField(default=0)),
                ('Hajmola', models.IntegerField(default=0)),
                ('Seacod', models.IntegerField(default=0)),
                ('Shelcal', models.IntegerField(default=0)),
                ('Crocin', models.IntegerField(default=0)),
                ('Lubrifresh', models.IntegerField(default=0)),
                ('Dettol', models.IntegerField(default=0)),
                ('Ashwagandha', models.IntegerField(default=0)),
                ('Moov', models.IntegerField(default=0)),
                ('Zandu', models.IntegerField(default=0)),
                ('Vicks', models.IntegerField(default=0)),
                ('Chyawanprash', models.IntegerField(default=0)),
                ('totalSum', models.IntegerField(default=0)),
            ],
        ),
    ]
