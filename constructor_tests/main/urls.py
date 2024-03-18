from django.urls import path
from .views import vote, about, contact, index, detail, results, add_tests, add_question, add_valuation, \
    DemoListQuestions, DemoTest, DemoValuation, add_final, UpdateTest, update_question, UpdateValuation # IndexView, DetailView, ResultsView,




urlpatterns = [
    # path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),


    path('', index, name='index'),
    path('<int:test_id>/test/<int:question_id>/', detail, name='detail'),
    path('<int:test_id>/test/results/', results, name='results'),
    path('<int:test_id>/test/<int:question_id>/vote/', vote, name='vote'),

    path('<int:test_id>/add-question/', add_question, name='add_question'),
    path('<int:test_id>/deno-list-questions/', DemoListQuestions.as_view(), name='demo_list_questions'),
    path('<int:test_id>/<int:question_id>/update-question/', update_question, name='update_question'),

    path('add-tests/', add_tests, name='add_tests'),
    path('<int:test_id>/demo-test/', DemoTest.as_view(), name='demo_test'),
    path('<int:test_id>/update-test/', UpdateTest.as_view(), name='update-test'),

    path('<int:test_id>/add-valuation/', add_valuation, name='add_valuation'),
    path('<int:test_id>/demo-valuation/', DemoValuation.as_view(), name='demo_valuation'),
    path('<int:test_id>/<int:valuation_id>/update-valuation/', UpdateValuation.as_view(), name='update_valuation'),
    path('<int:test_id>/add-final/', add_final, name='add_final'),

    # path('<int:test_id>/update-whole-test/', update_whole_test, name='update_whole_test'),
]
