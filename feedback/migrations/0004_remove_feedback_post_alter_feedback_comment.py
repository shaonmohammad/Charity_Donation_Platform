# Generated by Django 4.2.3 on 2023-09-28 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_alter_feedback_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='post',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='comment',
            field=models.CharField(max_length=300),
        ),
    ]
