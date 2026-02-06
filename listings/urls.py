from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:property_id>', views.property_detail, name='property'),
    path('about', views.about, name='about'),
]