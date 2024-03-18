from django.urls import path
from .views import (index, about, contact, vote, detail,
                    results, add_tests, add_question, add_valuation,
                    DemoListQuestions, DemoTest, DemoValuation, add_final,
                    UpdateTest, update_question, UpdateValuation)




urlpatterns = [
    path('', index, name='index'), # Главная странца (пока переадресация на 'catalog'
    path('about/', about, name='about'), # О проеке (пока заглушка)
    path('contact/', contact, name='contact'), # Контакты (пока заглушка)

    path('<int:test_id>/test/<int:question_id>/', detail, name='detail'), # Просмотр теста
    path('<int:test_id>/test/<int:question_id>/vote/', vote, name='vote'), # Прохождение теста
    path('<int:test_id>/test/results/', results, name='results'), # Представление резульатов теста

    path('add-tests/', add_tests, name='add_tests'), # Добавление теста
    path('<int:test_id>/demo-test/', DemoTest.as_view(), name='demo_test'), # Предпросмотр теста
    path('<int:test_id>/update-test/', UpdateTest.as_view(), name='update-test'), # Редактирование теста

    path('<int:test_id>/add-question/', add_question, name='add_question'), # Добавление вопрооса
    path('<int:test_id>/deno-list-questions/', DemoListQuestions.as_view(), name='demo_list_questions'), # Предпросмотр списка добавленных вопросов
    path('<int:test_id>/<int:question_id>/update-question/', update_question, name='update_question'), # Редактирование вопрооса

    path('<int:test_id>/add-valuation/', add_valuation, name='add_valuation'), # Добавление оценок
    path('<int:test_id>/demo-valuation/', DemoValuation.as_view(), name='demo_valuation'), # Предпросмотр списка оценок
    path('<int:test_id>/<int:valuation_id>/update-valuation/', UpdateValuation.as_view(), name='update_valuation'), # Редактироване оценок
    path('<int:test_id>/add-final/', add_final, name='add_final'), # Представление результатов пройденного теста

    # path('<int:test_id>/update-whole-test/', update_whole_test, name='update_whole_test'),
]
