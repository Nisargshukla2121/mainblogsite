# Generated by Django 3.1.5 on 2021-02-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0043_auto_20210216_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]