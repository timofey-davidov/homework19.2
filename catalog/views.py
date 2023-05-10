from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    response = render_to_string('catalog/home.html')
    return HttpResponse(response)

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Ура! Новый пользователь {name} с телефоном {phone} отправил сообщение: {message}")
    return render(request, 'catalog/contacts.html')