from django.shortcuts import render
from .models import Person

def homeview(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']

        p = Person(name=name, age=age, address=address)
        p.save()

    data = Person.objects.all()
    return render(request, 'home.html', {'persons': data})
