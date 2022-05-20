from django import forms
from orders.models import Order  # свяжем форму и модель, создадим class Meta
from trackers.models import Tracker


class OrderForm(forms.ModelForm):
    personal_data = forms.BooleanField(label="Я согласен на обработку персональных данных", required=True)  # логическое поле BooleanField. По умолчанию лог поля выводятся с помощью <input type="checkbox">. У нашего поля название label=.  required=True - обязательно до заполнения.
    tracker = forms.ModelChoiceField(queryset=Tracker.objects.all(), widget=forms.HiddenInput)  # создали поле tracker, что является полем выбора из всех трекеров, за что отвечает эта строка. В качестве widget используем скрытый HiddenInput а не селект как раньше

    class Meta:
        model = Order  # - модель и форма связаны, теперь укажем поля, которые нужно выводить
        fields = ["tracker", "name", "phone"]
