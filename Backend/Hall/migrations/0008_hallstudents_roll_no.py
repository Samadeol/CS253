# Generated by Django 4.0.3 on 2022-03-18 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hall', '0007_alter_hallpresence_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='hallstudents',
            name='roll_no',
            field=models.IntegerField(null=True),
        ),
    ]