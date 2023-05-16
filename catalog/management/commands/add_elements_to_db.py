from django.core.management import BaseCommand, call_command
from catalog.models import Product, Category

class Command(BaseCommand):
    def handle(self, *args, **options):
        # удаляем элементы из БД
        Category.objects.all().delete()
        Product.objects.all().delete()
        call_command('loaddata', 'data.json')