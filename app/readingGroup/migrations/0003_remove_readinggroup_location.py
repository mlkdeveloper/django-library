# Generated by Django 3.2.16 on 2023-02-12 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readingGroup', '0002_alter_readinggroup_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readinggroup',
            name='location',
        ),
    ]
