from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import CreateContactForm
from .models import ContactInfo
# Create your views here.

def home(request):
    return render(request, 'phonebook/home.html')

def create_contact(request):
    if request.method == 'POST':
        form = CreateContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()

            messages.success(request, f'Contact Created Successfuly!')
            return redirect('home')    
    else:
        form = CreateContactForm()

    context = {'form': form}
    return render(request, 'phonebook/create_contact.html', context)

def list_contacts(request):
    context ={}
 
    # add the dictionary during initialization
    context["contacts"] = ContactInfo.objects.filter(user=request.user).all()
         
    return render(request, "phonebook/list_contacts.html", context)

def delete_contact(request, contact_id):
    
    contact = ContactInfo.objects.get(id = contact_id)
    contact.delete()
    return redirect('/')
