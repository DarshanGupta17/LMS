# Generated by Django 4.2.3 on 2024-03-01 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_student_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(default=0, upload_to='media/profile_pic'),
        ),
    ]
