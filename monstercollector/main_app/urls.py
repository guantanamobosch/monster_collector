from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('monsters/', views.monsters_index, name='index'),
    path('monsters/<int:monster_id>', views.monsters_detail, name='detail'),
    path('monsters/create/', views.MonsterCreate.as_view(), name='monsters_create'),
    path('monsters/<int:pk>/update/', views.MonsterUpdate.as_view(), name='monsters_update'),
    path('monsters/<int:pk>/delete/', views.MonsterDelete.as_view(), name='monsters_delete'),
    path('monsters/<int:monster_id>/add_loot', views.add_loot, name='add_loot'),
    path('monsters/<int:monster_id>/assoc_dungeon/<int:dungeon_id>/', views.assoc_dungeon, name='assoc_dungeon'),
]