# Generated by Django 3.1 on 2020-08-22 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesweb', '0004_auto_20200822_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='name',
            field=models.CharField(blank=True, default='', max_length=80),
        ),
    ]