from django.apps import AppConfig


class ConstructorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'constructor'
    verbose_name = 'Конструктор тестов'  # Задаем отображение имени всего приложения, отображаемое в админке
