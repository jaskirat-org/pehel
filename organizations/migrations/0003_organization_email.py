# Generated by Django 4.0.3 on 2022-03-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_organization_photo_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='email',
            field=models.CharField(default='pehel@gmail.com', max_length=100),
        ),
    ]
