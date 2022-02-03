# Generated by Django 4.0.2 on 2022-02-03 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0001_initial'),
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=60, null=True)),
                ('credits', models.IntegerField()),
                ('department', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department')),
                ('instructors', models.ManyToManyField(db_table='course_instructor', related_name='courses', to='person.Person')),
            ],
        ),
    ]