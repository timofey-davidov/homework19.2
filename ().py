# coding: utf-8
Product.objects.get(pk=3)
Product.objects.get(pk=3).preview_image='catalog/bentsai.jpg'
Product.objects.get(pk=3).preview_image='catalog/bentsai.jpg'.save()
Product.objects.get(pk=3).preview_image
from django.core.files import File
item = Product.objects.filter(pk=3)
item.preview_image.save('abc.jpg', File(open('catalog/bentsai.jpg', 'r')))
item
item[0].preview_image.save('abc.jpg', File(open('catalog/bentsai.jpg', 'r')))
item[0].preview_image.save('abc.jpg', File(open('bentsai.jpg', 'r')))
item[0].preview_image.save('abc.jpg', File(open('media/catalog/bentsai.jpg', 'r')))
item[0].preview_image.save('abc.jpg', File(open('media/catalog/bentsai.jpg', 'rb')))
item[0].description.save('Принтер с хорощей моментальной печатью')
item[0].description='Принтер с хорошей моментальной печатью'
item.save()
