# Generated by Django 4.1 on 2022-08-29 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demonewsmodel',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
