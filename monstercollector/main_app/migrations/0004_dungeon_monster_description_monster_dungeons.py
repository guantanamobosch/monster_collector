# Generated by Django 4.1.7 on 2023-04-03 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_loot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dungeon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='monster',
            name='description',
            field=models.TextField(default='unknown'),
        ),
        migrations.AddField(
            model_name='monster',
            name='dungeons',
            field=models.ManyToManyField(to='main_app.dungeon'),
        ),
    ]
