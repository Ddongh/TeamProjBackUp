# Generated by Django 4.0.2 on 2022-02-07 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockpredapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code_name',
            name='stock_code',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='code_name',
            name='stock_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]