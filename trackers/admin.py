from django.contrib import admin
from trackers.models import Tracker # чтоб связать админку с моделью


@admin.register(Tracker) # связали класс TrackerAdmin с моделью с помощью декоратора
class TrackerAdmin(admin.ModelAdmin): # подключаем к админке приложение для управления домами. Для удобства указываем имя модели Tracker и слово Admin
    list_display = ["name", "price", "active"] # отвечает за поля модели, которые нужно выводить в админке. До добавления этого списка имя бралось через def __str__(self):. Но теперь __str__ не используется и видим чистое имя.
    list_filter = ["active"]  # добавили фильтр по полю active
