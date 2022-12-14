# Generated by Django 4.1.3 on 2022-12-09 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date started')),
                ('status', models.CharField(choices=[('OS', 'On Shelf'), ('SR', 'Started Reading'), ('FR', 'Finished Reading')], default='OS', max_length=2)),
            ],
        ),
    ]
