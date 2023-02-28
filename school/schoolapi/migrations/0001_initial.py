# Generated by Django 4.1.7 on 2023-02-27 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='school',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=30)),
                ('school_address', models.CharField(max_length=30)),
                ('teachers_list', models.DecimalField(decimal_places=0, max_digits=30)),
                ('total_students', models.DecimalField(decimal_places=0, max_digits=20)),
            ],
        ),
    ]
