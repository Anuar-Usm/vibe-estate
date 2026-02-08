from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Property

# 1. ГЛАВНАЯ СТРАНИЦА (ОБЯЗАТЕЛЬНО ДОЛЖНА БЫТЬ)
def index(request):
    queryset_list = Property.objects.order_by('-list_date').filter(is_published=True)
    context = {
        'listings': queryset_list
    }
    return render(request, 'listings/index.html', context)

# 2. СТРАНИЦА ОБЪЕКТА
def property(request, property_id):
    listing = get_object_or_404(Property, pk=property_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/property.html', context)

# 3. ПОИСК
def search(request):
    queryset_list = Property.objects.order_by('-list_date').filter(is_published=True)

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                Q(description__icontains=keywords) | Q(title__icontains=keywords)
            )

    if 'city' in request.GET:
        city = request.GET['city']
        if city and city != 'Город (Все)':
            queryset_list = queryset_list.filter(city__iexact=city)

    context = {
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)

# 4. СТРАНИЦА "О НАС"
def about(request):
    return render(request, 'listings/about.html')