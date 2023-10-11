# Generated by Django 4.2.3 on 2023-10-06 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_userinformation_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]
