# Generated by Django 4.2.2 on 2023-06-21 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='journaluseform',
            name='file',
            field=models.FileField(blank=True, upload_to='picture/'),
        ),
    ]
