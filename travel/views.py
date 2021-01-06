from django.shortcuts import render


def home(request):
    name = 'Bob'
    return render(request, 'home.html', {'name': name})

def about(request):
    about = 'About'
    return render(request, 'about.html', {'about': about})