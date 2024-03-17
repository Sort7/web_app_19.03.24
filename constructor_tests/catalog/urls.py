from django.urls import path

from .views import Test, category, TestsCatalog


urlpatterns = [
    path('', TestsCatalog.as_view(), name='catalog'),
    path('test/<int:test_id>/', Test.as_view(), name='test'),
    path('catalog/<int:category_id>/', category, name='category'),
    # path('test/<int:test_id>/tests-add/', tests_add, name='test_add'),
    # path('test/<int:test_id>/questions-add/', add_questions, name='add_questions'),
]