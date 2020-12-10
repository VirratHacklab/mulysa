# Generated by Django 3.1.4 on 2020-12-09 21:48

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20201209_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(error_messages={'unique': 'This phone number is already registered to a member'}, help_text='This number will also be the one that gets access to the hacklab premises. International format (+35840123567).', max_length=255, null=True, unique=True, validators=[users.models.validate_phone], verbose_name='Mobile phone number'),
        ),
    ]