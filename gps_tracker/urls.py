"""gps_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static  # чтоб сервер отдавал пользователю обычные файлы, картинки, документы, css. Функция static отвечает за обработку статических файлов
from django.conf import settings  # получили доступ к модулю settings, но не напрямую а через django.conf - рекомендация django
from trackers.views import trackers_list  # из trackers.views импортируем trackers_list
from trackers.views import tracker_detail  # связали представление с URL
# чтоб вьюха заработала ее связываем с адресом. До этого наша вьюха срабатывала на главной странице и выводила trackers_list.html. Чтоб вывести трекеры из БД, а доступ к БД осуществляется через модели, сначала надо импортировать модель в модуль views.py

# urlpatterns отвечает за URL пути что есть на сайте
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', trackers_list, name="tracker"),  # path связывает адрес страницы с представлением. 1 параметр - URL путь - пустая строка это главная страница. trackers_list - ф-я представления, что вызывается когда пользователь открывает главную страницу
    path("<int:tracker_id>", tracker_detail, name="tracker")  # применили пройтейший шаблон для нашего пути, который говорит, что мы ожидаем целое число, которое нужно поместить в агрумент tracker_id функции tracker_datail
]

# Подключим обработку медиафайлов.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # добавили еще один путь, что начинается с MEDIA_URL и обрабатывает статичные файлы в MEDIA_ROOT
