from django.contrib import admin

from constructor.models import Tests, Categories, Questions, Answers, Valuation, Result


class TestsAdmin(admin.ModelAdmin): # Настройка отображения полей модели в админ понели
    list_display = ('id', 'title', 'review', 'manual', 'time_create', 'is_published',) # Перечень полей отображаемых в админ понели
    list_display_links = ('id', 'title',) # Перечень полей с ссылками переходами для редактирования
    search_fields = ('title', 'review',) # Перечень полей по которым можно будет проводить поиск информации
    list_editable = ('is_published',) # Позволяет редактировать поле прямо таблице модели админки, без открытия окон
    list_filter = ('is_published', 'time_create',) # Создает список по которому можно фильтровать записи модели

# Регистриуем модель в админ понели (чтобы она через админку была доступна)
admin.site.register (Tests, TestsAdmin) # После добавления класса настройки отображения модели в админке,
                                        # его имя в качестве второго аргумента добавляется в эту функцию
admin.site.register (Categories)
admin.site.register (Questions)
admin.site.register (Answers)
admin.site.register (Valuation)
admin.site.register (Result)

