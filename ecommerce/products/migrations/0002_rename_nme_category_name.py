# Generated by Django 4.2.7 on 2023-11-30 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='nme',
            new_name='name',
        ),
    ]