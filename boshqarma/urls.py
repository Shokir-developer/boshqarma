from django.urls import path
from .views import index, news, hujjatlar, quyi_tashkilotlar

urlpatterns = [
	path('', index, name='index'),
	path('news/', news, name='news'),
	path('docs/', hujjatlar, name='hujjatlar'),
	path('branchs/', quyi_tashkilotlar, name='quyi_tashkilotlar'),
]
