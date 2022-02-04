# Generated by Django 4.0.2 on 2022-02-04 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockpredapp', '0002_alter_code_name_market'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code_name',
            name='homepage',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='code_name',
            name='industry',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='code_name',
            name='listing_date',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='code_name',
            name='market',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='code_name',
            name='region',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='code_name',
            name='representative',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='code_name',
            name='sector',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='code_name',
            name='settle_month',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
