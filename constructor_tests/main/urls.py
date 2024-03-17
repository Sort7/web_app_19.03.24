from django.urls import path
from .views import vote, about, contact, index, detail, results, add_tests, add_question, add_valuation, \
    DemoListQuestions, DemoTest, DemoValuation, add_final, UpdateTest, update_question, UpdateValuation # IndexView, DetailView, ResultsView,




urlpatterns = [
    # path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),


    path('', index, name='index'), # ex: /polls/
    # path('<int:question_id>/', detail, name='detail'), # ex: /polls/5/
    path('<int:test_id>/test/<int:question_id>/', detail, name='detail'), # ex: /polls/5/
    path('<int:test_id>/test/results/', results, name='results'), # ex: /polls/5/results/
    path('<int:test_id>/test/<int:question_id>/vote/', vote, name='vote'), # ex: /polls/5/vote/

    path('<int:test_id>/add-question/', add_question, name='add_question'), # ex: /polls/
    path('<int:test_id>/deno-list-questions/', DemoListQuestions.as_view(), name='demo_list_questions'),
    path('<int:test_id>/<int:question_id>/update-question/', update_question, name='update_question'),

    path('add-tests/', add_tests, name='add_tests'),
    path('<int:test_id>/demo-test/', DemoTest.as_view(), name='demo_test'),
    path('<int:test_id>/update-tests/', UpdateTest.as_view(), name='update_tests'),

    path('<int:test_id>/add-valuation/', add_valuation, name='add_valuation'),
    path('<int:test_id>/demo-valuation/', DemoValuation.as_view(), name='demo_valuation'),
    path('<int:test_id>/update-valuation/', UpdateValuation.as_view(), name='update_valuation'),
    path('<int:test_id>/add-final/', add_final, name='add_final'),


    # path('', IndexView.as_view(), name='index'),
    # path('<int:pk>/', DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', vote, name='vote'),
]
