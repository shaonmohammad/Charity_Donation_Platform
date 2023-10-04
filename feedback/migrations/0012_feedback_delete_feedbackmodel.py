# Generated by Django 4.2.3 on 2023-10-03 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0011_remove_feedbackmodel_blog_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='FeedbackModel',
        ),
    ]
