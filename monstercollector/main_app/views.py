from django.shortcuts import render

monsters = [
    {'name': 'Aartuk Elder', 'type': 'Plant', 'size': 'Large', 'alignment': 'Typically Lawful Evil'},
    {'name': 'Adult Blue Dracolich', 'type': 'Undead', 'size': 'Huge', 'alignment': 'Lawful Evil'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def monsters_index(request):
    return render(request, 'monsters/index.html', {
        'monsters': monsters
    })