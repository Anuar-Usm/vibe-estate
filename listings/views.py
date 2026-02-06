from django.shortcuts import render, get_object_or_404
from .models import Property

def index(request):
    # Добавляем .filter(is_published=True), чтобы скрытые объекты не попадали в каталог
    queryset_list = Property.objects.order_by('-list_date').filter(is_published=True)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    if 'property_type' in request.GET:
        p_type = request.GET['property_type']
        if p_type:
            queryset_list = queryset_list.filter(property_type__iexact=p_type)

    if 'rooms' in request.GET:
        rooms = request.GET['rooms']
        if rooms:
            queryset_list = queryset_list.filter(rooms__iexact=rooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'properties': queryset_list
    }
    return render(request, 'listings/index.html', context)

def property_detail(request, property_id):
    # Здесь тоже проверяем is_published=True, чтобы нельзя было зайти на объект по прямой ссылке, если он скрыт
    property = get_object_or_404(Property, pk=property_id, is_published=True)
    
    context = {
        'property': property
    }
    return render(request, 'listings/property.html', context)

def about(request):
    return render(request, 'listings/about.html')