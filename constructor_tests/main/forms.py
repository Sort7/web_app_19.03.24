from django import forms
from .models import Tests, Questions, Choice, Valuation


class AddTestsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category_key'].empty_label = "Категория не выбрана"
        self.fields['category_key'].label = "Категория теста"

    class Meta:
        model = Tests
        fields = {'title', 'review', 'manual', 'number_of_questions', 'number_of_сhoice', 'category_key',
                  'is_published', }

    field_order = ['title', 'review', 'manual', 'category_key', 'number_of_questions', 'number_of_сhoice',
                   'is_published', ]

    title = forms.CharField(max_length=255, label="Название теста",
                            widget=forms.TextInput(attrs={'class': 'form-input', 'cols': 70, }))
    review = forms.CharField(required=False, label="Описание теста",
                             widget=forms.Textarea(attrs={'cols': 70, 'rows': 5}))
    manual = forms.CharField(required=False, label="Инструкция прохождения",
                             widget=forms.Textarea(attrs={'cols': 70, 'rows': 5}))
    number_of_questions = forms.IntegerField(label="Количество вопросов")
    number_of_сhoice = forms.IntegerField(label="Количество ответов")
    is_published = forms.BooleanField(label="Опубликовать")


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = {'question_ordinal', 'question_text'}

    field_order = ['question_ordinal', 'question_text']

    question_ordinal = forms.IntegerField(label="Порядковый номер")
    question_text = forms.CharField(label="Вопрос",
                                    widget=forms.Textarea(attrs={'class': 'form-input'}))


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = {'choice_ordinal', 'choice_text', 'ball'}

    field_order = ['choice_ordinal', 'choice_text', 'ball']

    choice_text = forms.CharField(max_length=255, label="Вариант ответа",
                                  widget=forms.TextInput(attrs={'class': 'form-input', 'cols': 50, }))
    choice_ordinal = forms.IntegerField(label="Порядковый номер")
    ball = forms.IntegerField(label="Балл ответа")


class AddValuationForm(forms.ModelForm):
    class Meta:
        model = Valuation
        fields = {'valuation', 'value_max', 'analysis'}

    field_order = ['valuation', 'value_max', 'analysis']

    valuation = forms.CharField(max_length=255, label="Уровень результата",
                                widget=forms.TextInput(attrs={'class': 'form-input'}))
    value_max = forms.IntegerField(label="Верхняя граница")
    analysis = forms.CharField(required=False, label="Интерпритация оценки",
                               widget=forms.Textarea(attrs={'cols': 70, 'rows': 5}))
