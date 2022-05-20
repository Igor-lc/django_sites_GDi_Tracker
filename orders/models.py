from django.db import models
from trackers.models import Tracker

class Order(models.Model):
    tracker = models.ForeignKey(Tracker, verbose_name="трекер", on_delete=models.CASCADE)  # создали внешний ключ на трекер, то есть модель Order теперь связана моделью Tracker, а сама заявка теперь будет хранить идентификатор дома, к которому она относится.  on_delete=models.CASCADE отвечает за поведение таблицы Orders при удалении дома. Если посетитель оставит заявку на трекер, а потом мы решим удалить его из базы, то удаление повлечет за собой каскадное удаление всех заявок, что с ним связаны
    name = models.CharField("имя", max_length=50)
    phone = models.CharField("телефон", max_length=50)
    date = models.DateTimeField("дата", auto_now_add=True)  # добавили поле для хранения даты и времени заявки и указали, чтоб оно автоматически создавалось датой создания заявки. Теперь добавим наше приложение orders список INSTALLED_APPS, после чего выполним миграцию.
