# Generated by Django 4.2.19 on 2025-03-10 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_id',
            new_name='isbn',
        ),
    ]
