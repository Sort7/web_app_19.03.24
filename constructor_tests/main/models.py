import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import PositiveIntegerField
from django.utils import timezone
from django.urls import reverse


class Categories (models.Model):
    category = models.CharField(max_length=250, db_index=True)  # Названия категории

    def __str__(self):
        return self.category

    def get_absolute_url (self):
        return reverse ('category', kwargs={'category_id': self.pk})


class Tests(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название теста") # Названия теста
    review = models.TextField(blank=True, verbose_name="Отписание теста")  # Описания теста
    manual = models.TextField(blank=True, verbose_name="Инструкция по выполеннию теста")  # Инструкции по прохождению теста
    number_of_questions = models.PositiveIntegerField(verbose_name="Количество вопросов в тесте")  # Количества вопросов в тесте
    number_of_сhoice = models.PositiveIntegerField(verbose_name="Количество вариантов ответа")  # Количества вариантов ответа
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    category_key = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True, verbose_name="Категория")
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='author_test', null=True, default=None, verbose_name="Автор")
    is_published = models.BooleanField(default=True) # Отметка о публикации

    def __str__(self):
        return self.title

    def get_absolute_url (self):
        return reverse ('test', kwargs={'test_id': self.pk})

    class Meta: # Задаем настройки отображения модел в понели администратора.
        verbose_name = 'Тесты' # Задаем отображение имени модели в единственном числе.
        verbose_name_plural = 'Тесты' # Задаем отображение имени модели во множественном числе.
        # ordering = ['time_create', 'title'] # Задаем порядок отображения тестов в списке (первично по дате добавления, вторично по имени).



# class Cat(models.Model): # Модель категории (аналог Тестов)
#     cat_name = models.CharField(max_length=200)  # Тест вопрооса
#
#     def __str__(self):
#         return self.cat_name


class Questions(models.Model):
    test_key = models.ForeignKey('Tests', on_delete=models.PROTECT, null=True)
    question_ordinal = models.PositiveIntegerField(verbose_name="Порядковый номер")  # Порядковый номер вопроса
    question_text = models.TextField(blank=True, verbose_name="Текст вопроса")  # Текст вопроса

    def __str__(self):
        return self.question_text


# class Quest(models.Model): # Модель вопросов при опросе
#     cat_key = models.ForeignKey(Cat, default=1, on_delete=models.CASCADE)
#     question_text = models.CharField(max_length=200)  # Тест вопрооса
#     pub_date = models.DateTimeField('date published') # Дата публикации
#
#     def __str__(self):
#         return self.question_text


class Choice(models.Model): # Модель вариантов ответа
    question_key = models.ForeignKey(Questions, on_delete=models.CASCADE)  # Ключ связки с моделью вопросов
    test_key = models.ForeignKey(Tests, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name="Вариант ответа") # Текст варианта ответа
    choice_ordinal = models.PositiveIntegerField(verbose_name="Порядковый номер")
    ball = models.IntegerField(default=0, verbose_name="Балл за ответ") # Балл ответа

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Result(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='user_test', null=True, default=None)
    result = models.IntegerField(default=0,  verbose_name="Результат")  # Набранные баллы при прохождении теста
    the_best_result = models.IntegerField(verbose_name="Лучший результата")  # Лучший балл пользователя при прохождении теста
    test_key = models.ForeignKey('Tests', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.user



# class Rez (models.Model): # Модель результатов
#     rez_ball = models.IntegerField(default=0) # Итоговый баллл
#     user = models.CharField(max_length=200) # Пользователь
#     question = models.ForeignKey(Quest, default=1, on_delete=models.CASCADE)
#     cat_key = models.ForeignKey(Cat, default=1, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.user


class Valuation(models.Model):
    valuation = models.CharField(max_length=250, verbose_name="Уровень результата")  # Обобщенная оценка результата
    value_max = models.PositiveIntegerField(verbose_name="Верхняя граница")  # Верхняя граница значений
    analysis = models.TextField(blank=True, verbose_name="Интерпритация оценки")  # Описние анализа результата
    test_key = models.ForeignKey('Tests', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.valuation

    def get_absolute_url (self):
        return reverse ('update_valuation', kwargs={'test_id': self.pk})