from django import forms


class TrackersFilterForm(forms.Form):  # создали форму не на основе модели, а простую, которую будем обрабатывать вручную
    min_price = forms.IntegerField(label="Фильтр по цене, от", required=False)
    max_price = forms.IntegerField(label="Фильтр по цене, до", required=False)  # required=False - данные можно не заполнять. Теперь передадим форму в шаблон через представление
    query = forms.CharField(label="Поиск", required=False)  # добавили в форму необязательное текстовое поле query, которое будет выводится с помощью <input type="text">. В Django есть 2 типа текстовых полей: CharField - для поисковых полей, коротких данных и  TextField - для относительно больших текстовых данных
    ordering = forms.ChoiceField(label="Сортировка", required=False, choices=[
        ("name", "по алфавиту"),
        ("price", "дешевые сверху"),
        ("-price", "дорогие сверху")
    ])  # добавил поле ordering чтоб менять порядок сортировки через форму фильтрации. Создал поле выбора CharField, что на сайте будет выводится в html елементе select
