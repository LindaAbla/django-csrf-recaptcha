# Generated by Django 3.2.16 on 2023-05-02 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='private_access_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]