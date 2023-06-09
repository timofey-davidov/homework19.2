# Generated by Django 4.2.1 on 2023-05-29 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_product_image_alter_product_preview_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='change_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
    ]
