# Generated by Django 4.2 on 2023-04-10 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('autor', models.CharField(max_length=30)),
                ('publicacion', models.IntegerField()),
                ('editorial', models.CharField(max_length=30)),
            ],
        ),
    ]
