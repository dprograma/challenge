# Generated by Django 4.1 on 2022-08-31 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_demonewsmodel_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='demonewsmodel',
            options={'ordering': ['-created_at']},
        ),
    ]