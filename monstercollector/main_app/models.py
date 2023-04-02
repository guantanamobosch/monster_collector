from django.db import models
from django.urls import reverse

# Create your models here.
class Monster(models.Model):
    name = models.CharField(max_length=100, default='unknown')
    type = models.CharField(max_length=50, default='unknown')
    size = models.CharField(max_length=10, default='unknown')
    alignment = models.CharField(max_length=50, default='unknown')
    armor_class = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'monster_id': self.id})
    
class Loot(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.monster} hoards {self.name}"