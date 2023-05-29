from catalog.apps import CatalogConfig
from django.urls import path

from catalog.views import home, contacts, card

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/item/', card, name="card")
]