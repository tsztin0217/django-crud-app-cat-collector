# main_app/views.py

from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat

# Import HttpResponse to send text-based responses
# from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
    # each view function or "view"
    # recieves a request object
    # return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')
    # to send a response, we return it!
    return render(request, 'home.html')


def about(request):
    contact_details = 'you can reach support at support@catcollector.com'
    return render(request, 'about.html', {
        'contact': contact_details
    })


# Create a simple Cat class and a list of cat instances to simulate a database of cats

# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# # Create a list of Cat instances
# cats = [
#     Cat('Lolo', 'tabby', 'Kinda rude.', 3),
#     Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
#     Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
#     Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
# ]


# Everything in a Python module is automatically exported, 
# thus, the Cat class and the cats list will be accessible in other modules.

def cat_index(request):
    cats = Cat.objects.all();
    # Render the cats/index.html template with the cats data
    return render(request, 'cats/index.html', {'cats': cats})



def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})


class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']

class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'