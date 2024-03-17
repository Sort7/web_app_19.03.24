from django import forms
from constructor.models import Tests, Questions

class AddTestsForm (forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"
        self.fields['category'].label = "Категория теста"


    class Meta:
        model = Tests
        fields = {'title', 'review', 'manual', 'number_of_questions','category', 'is_published'}

    field_order = ['title', 'review', 'manual', 'category', 'number_of_questions', 'is_published']

    title = forms.CharField(max_length=255, label="Название теста",
                            widget=forms.TextInput(attrs={'class': 'form-input'}))
    review = forms.CharField(required=False, label="Описание теста",
                             widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}))
    manual = forms.CharField(required=False, label="Инструкция прохождения",
                             widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}))
    number_of_questions = forms.IntegerField(label="Количество вопросов")
    is_published = forms.BooleanField(label="Опубликовать")



class AddQuestionsForm (forms.ModelForm):

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.fields['test'].empty_label = "Тест не выбран"
         self.fields['test'].label = "Выбор теста"


    class Meta:
        model = Questions
        fields = {'question_ordinal', 'question_text', 'test'}


    field_order = ['question_ordinal', 'question_text', 'test']

    question_ordinal = forms.IntegerField(label="Порядковый номер вопроса")
    question_text = forms.CharField(required=False, label="Текст вопроса",
                             widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}))
