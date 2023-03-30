from django.db import models

# Create your models here.
class Monster(models.Model):
    name = models.CharField(max_length=100, default='unknown')
    type = models.CharField(max_length=50, default='unknown')
    size = models.CharField(max_length=10, default='unknown')
    alignment = models.CharField(max_length=50, default='unknown')
    armor_class = models.IntegerField()

    def __str__(self):
        return self.name