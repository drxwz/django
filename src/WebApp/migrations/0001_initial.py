# Generated by Django 3.0.7 on 2020-06-06 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_adress', models.CharField(max_length=100)),
                ('client_email', models.CharField(max_length=100)),
                ('client_phone', models.CharField(max_length=100)),
            ],
        ),
    ]