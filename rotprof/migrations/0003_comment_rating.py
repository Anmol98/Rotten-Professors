# Generated by Django 2.0.13 on 2019-03-27 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotprof', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
