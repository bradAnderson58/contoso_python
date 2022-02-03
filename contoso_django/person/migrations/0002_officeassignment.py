# Generated by Django 4.0.2 on 2022-02-03 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeAssignment',
            fields=[
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='person.person')),
                ('location', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
