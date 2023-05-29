from django.db import models
from django.core.files.storage import FileSystemStorage

NULLABLE = {'blank': True, 'null': True}
_MAX_SIZE = 300 # максимальный размер изображения


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    preview_image = models.ImageField(upload_to='media/', verbose_name='Превью-изображение', **NULLABLE)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE, max_length=20, verbose_name = "Категория", **NULLABLE)
    price = models.FloatField(verbose_name = "Стоимость", **NULLABLE)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата создания', **NULLABLE)
    change_date = models.DateTimeField(auto_now=True, verbose_name = 'Дата изменения', **NULLABLE)

    def __str__(self):
        return f"Продукт {self.title} из категории {self.product_category} по цене {self.price}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('-price',)

class Category(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(**NULLABLE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('title',)

class Contact(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50)
    phone = models.CharField(verbose_name='Телефон', max_length=50)

    def __str__(self):
        return f'Имя: {self.name}, телефон: {self.phone}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ('name',)


