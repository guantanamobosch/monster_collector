from django.forms import ModelForm
from .models import Loot

class LootForm(ModelForm):
    class Meta:
        model = Loot
        fields = ['name', 'description']