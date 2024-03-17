from django.urls import path

from .views import Test, category, TestsCatalog


urlpatterns = [
    path('', TestsCatalog.as_view(), name='catalog'),
    path('test/<int:test_id>/', Test.as_view(), name='test'),
    path('catalog/<int:category_id>/', category, name='category'),
]