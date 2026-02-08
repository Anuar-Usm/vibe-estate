from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Эта строка ищет views.index
    path('<int:property_id>/', views.property, name='property'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
]