from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Monster
from .forms import LootForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def monsters_index(request):
    monsters = Monster.objects.all()
    return render(request, 'monsters/index.html', {
        'monsters': monsters
    })

def monsters_detail(request, monster_id):
    monster = Monster.objects.get(id=monster_id)
    loot_form = LootForm()
    return render(request, 'monsters/detail.html', { 'monster': monster, 'loot_form': loot_form })

def add_loot(request, monster_id):
    form = LootForm(request.POST)
    if form.is_valid():
        new_loot = form.save(commit=False)
        new_loot.monster_id = monster_id
        new_loot.save()
    return redirect('detail', monster_id=monster_id)

class MonsterCreate(CreateView):
    model = Monster
    fields = '__all__'

class MonsterUpdate(UpdateView):
    model = Monster
    fields = ['type', 'size', 'alignment', 'armor_class']

class MonsterDelete(DeleteView):
    model = Monster
    success_url = '/monsters'

