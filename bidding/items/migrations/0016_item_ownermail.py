# Generated by Django 3.0.3 on 2020-03-19 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0015_auto_20200319_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='ownermail',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
    ]
