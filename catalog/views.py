from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import Product


# Create your views here.
def home(request):
    all_items = Product.objects.all()
    return render(request, 'catalog/home.html', context={"all_items": all_items, "title": "Главная страница"})

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Ура! Новый пользователь {name} с телефоном {phone} отправил сообщение: {message}")
    return render(request, 'catalog/contacts.html')

def card(request, pk):
    all_items = Product.objects.filter(id=pk)
    title = all_items[0].title
    return render(request, 'catalog/card.html', context={"all_items": all_items, "title": title})