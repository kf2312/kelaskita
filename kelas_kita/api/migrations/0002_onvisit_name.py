# Generated by Django 3.1.4 on 2020-12-10 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='onvisit',
            name='name',
            field=models.CharField(default='test', max_length=50),
        ),
    ]