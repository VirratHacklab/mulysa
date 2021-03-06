# Generated by Django 3.1.4 on 2020-12-09 20:45

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20201114_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(help_text='This number will also be the one that gets access to the hacklab premises. International format (+35840123567).', max_length=255, null=True, unique=True, validators=[users.models.validate_phone], verbose_name='Mobile phone number'),
        ),
    ]
