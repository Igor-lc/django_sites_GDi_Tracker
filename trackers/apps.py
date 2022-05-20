from django.apps import AppConfig


# отвечает за общие настройки приложения
class TrackersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trackers'
    verbose_name = "Трекеры" # чтоб в админке переименовать названия приложений, trackers на Трекеры
