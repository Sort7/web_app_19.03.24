from django.urls import path

from .views import add_answers, tests_add  # QuestionsFormView, add_questions # tests_add

urlpatterns = [
    path('', tests_add, name='tests_add'),
    # path('<int:question_id>/add-questions/', add_questions, name='add_questions'),
    path('<int:question_id>/add-answers/', add_answers, name='add_answers'),


    # path('', index, name='index'),
    # path('<int:question_id>/', detail, name='detail'),
    # path('<int:question_id>/results/', results, name='results'),
    # path('<int:question_id>/vote/', vote, name='vote'),

    # path('add-tests/', tests_add, name='tests_add'),
    # path('add-tests/add-questions/', add_questions, name='add_questions'),
    # path('add-answers/', add_answers, name='add_answers'),
]