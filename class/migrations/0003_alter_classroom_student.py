# Generated by Django 4.1.1 on 2022-09-28 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_options_alter_student_table'),
        ('class', '0002_classroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='student',
            field=models.ManyToManyField(limit_choices_to=2, to='students.student'),
        ),
    ]
