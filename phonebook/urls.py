from django.urls import path, include
from .views import create_contact, home, list_contacts, delete_contact

urlpatterns = [
    path('', home, name = 'home'),
    path('auth/', include("users.urls")),
    path('create-contact/', create_contact, name='create-contact'),
    path('list-contacts/', list_contacts, name='list_contacts'),
    path('show-contact/<int:contact_id>', delete_contact, name='delete-contact')

]