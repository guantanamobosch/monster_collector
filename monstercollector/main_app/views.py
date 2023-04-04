from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Monster, Dungeon
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

def dungeons_index(request):
    dungeons = Dungeon.objects.all()
    return render(request, 'dungeons/index.html', {
        'dungeons': dungeons
    })

def monsters_detail(request, monster_id):
    monster = Monster.objects.get(id=monster_id)
    id_list = monster.dungeons.all().values_list('id')
    uninhabited_dungeons = Dungeon.objects.exclude(id__in=id_list)
    loot_form = LootForm()
    return render(request, 'monsters/detail.html', { 'monster': monster, 'loot_form': loot_form, 'dungeons': uninhabited_dungeons })

def add_loot(request, monster_id):
    form = LootForm(request.POST)
    if form.is_valid():
        new_loot = form.save(commit=False)
        new_loot.monster_id = monster_id
        new_loot.save()
    return redirect('detail', monster_id=monster_id)

class DungeonDetail(DetailView):
    model = Dungeon
    
class DungeonCreate(CreateView):
    model = Dungeon
    fields = '__all__'

class DungeonUpdate(UpdateView):
    model = Dungeon
    fields = ['name', 'description']

class DungeonDelete(DeleteView):
    model = Dungeon
    success_url = '/dungeons'

class MonsterCreate(CreateView):
    model = Monster
    fields = ['name', 'type', 'size', 'alignment', 'description', 'armor_class']

class MonsterUpdate(UpdateView):
    model = Monster
    fields = ['type', 'size', 'alignment', 'armor_class']

class MonsterDelete(DeleteView):
    model = Monster
    success_url = '/monsters'

def assoc_dungeon(request, monster_id, dungeon_id):
    Monster.objects.get(id=monster_id).dungeons.add(dungeon_id)
    return redirect('detail', monster_id=monster_id)