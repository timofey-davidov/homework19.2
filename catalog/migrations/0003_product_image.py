# Generated by Django 4.2.1 on 2023-05-28 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_contact_alter_category_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Изображение'),
        ),
    ]
