# view - представление или вьюха. Это функция на языке Python, что генерирует страницу и возвращает ее пользователю. Отвечает за отображение данных на сайте

from django.shortcuts import render, get_object_or_404
from trackers.models import Tracker
from orders.forms import OrderForm
from django.http import HttpResponseRedirect  # создаем редирект
from django.urls import reverse  # создаем редирект. В представлении после сохранения кода напишем
from trackers.forms import TrackersFilterForm
from django.db.models import Q  # импортировали клас Q чтоб поиск работал и по названию, не только по описанию. Q от Qery позволяет создавать сложные фильтры с использованием оператора or. Ниже фильтры используют оператор AND. Обернем в Q параметр поиска ниже


'''создадим первое представление что будет выводить все трекеры. Даже пустое всегда обязательно принимает один аргумент. request - http запрос посетителя сайта
Чтоб вернуть html страницу ее нужно создать - добавим в папке trackers папку templates для хранения шаблонов html документов.
Архитектура Django требует добавить в templates еще одну папку с тем же именем что и наше приложение - trackers
Имя представления trackers_list совпадает с именем шаблона, чтоб лучше ориентироваться в коде'''


def trackers_list(request):
    trackers = Tracker.objects.filter(active=True) # создаем запрос к БД с помощью ORM на получение всех объектов с помощью SQL запроса (такой набор данных называется queryset) и присваиваем переменной trackers. Tracker - это модель наших данных, мост между БД и Python. all меняем на filter(active=True)
    form = TrackersFilterForm(request.GET)  # параметр request.GET нужен чтобы не очищать форму после поиска
    if form.is_valid():  # добавим валидацию для применения фильтра. is_valid проверяет верные ли переданные данные, если да то Django поместит их в словарь cleaned_data
        if form.cleaned_data["min_price"]:  # проверяем передана ли цена
            trackers = trackers.filter(price__gte=form.cleaned_data["min_price"])  # - фильтруем по полю price.  __gte - интересуют те трекеры, цена которых больше равна form.cleaned_data["min_price"]
        if form.cleaned_data["max_price"]:
            trackers = trackers.filter(price__lte=form.cleaned_data["max_price"])  # gte - Greater than or equal. lte - Less than or equal.
        if form.cleaned_data["query"]:  # добавим еще одно условие фильтрации
            trackers = trackers.filter(
                Q(description__icontains=form.cleaned_data["query"]) |  # ищем по описанию,  | - отвечает за or. Ниже ищем по названию
                Q(name__icontains=form.cleaned_data["query"]))  # фильтруем по данным в поле description.  __icontains - ищем по всему тексту описания без учета регистра. Другие режимы поиска: __contains, __exact, __iexact
        if form.cleaned_data["ordering"]:  # добавим еще один фильтр
            trackers = trackers.order_by(form.cleaned_data["ordering"])  # применили метод order_by, отвечающий за сортировку данных. В него передаем имя столбца и порядок сортировки для сортировки

    # for tracker in trackers:
        # print(tracker.name, tracker.price) # print внутри вьюхи выводит данные в консоль. Теперь выведем их на сайт и сначала передадим список трекеров в шаблон. Добавим ниже в render 3 параметр - словарь.
    return render(request, "trackers/trackers_list.html", {"trackers": trackers, "form": form}) # возвращаем результат работы функции render, что принимает запрос пользователя request и название шаблона.
    # Связали представление с шаблоном, теперрь нужно связать его с URL - задать адрес по которому будет доступет список трекеров.


# Добавим каждому трекеру отдельную страницу
def tracker_detail(request, tracker_id):
    # перенесли получение объекта дома до создания формы:
    tracker = get_object_or_404(Tracker, id=tracker_id, active=True)  # если объукт с таким id будет найден, то get_object_or_404 вернет его в переменную tracker, если не найден, то вьюха вернет страницу 404. Теперь подключим строкой ниже шаблон. active=True - Django будет возвращать трекер только если найдет его id и он будет активен
    form = OrderForm(request.POST or None, initial={"tracker": tracker})  # request.POST or None - чтоб сохранить информацию в БД из формы на сайте. initial={"tracker": tracker} - чтоб формировать значение по умолчанию при создании формы

    if request.method == "POST":  # чтоб проверить входящие данные, все ли заполнено, есть ли номер телефона
        if form.is_valid():
            form.save()
            # reverse - аналог тега URL из шаблонов: {% url 'tracker' tracker_id=tracker.id %}
            url = reverse("tracker", kwargs={"tracker_id": tracker.id})  # сообщаем меткой что редирект прошел
            return HttpResponseRedirect(f"{url}?sent=1")   # reverse("tracker", kwargs={"tracker_id": tracker.id}) адрес на который нужно сделать редирект. Произойдет перезагрузка страницы с помощью метода GET и данные формы переданные POST запросом будут обнулены.  {url}?sent=1 - добавляем к URL адресу дополнительный параметр send со значением 1, теперь его надо отследить в URL адресе
    return render(request, "trackers/tracker_detail.html", {
            "tracker": tracker,
            "form": form,
            "sent": request.GET.get("sent")  # проверяем наличие sent в списке получаемых GET параметров
        })
