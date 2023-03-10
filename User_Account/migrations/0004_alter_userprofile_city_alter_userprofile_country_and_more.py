# Generated by Django 4.1.7 on 2023-03-08 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("User_Account", "0003_userprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="city",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="country",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="pin_code",
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
