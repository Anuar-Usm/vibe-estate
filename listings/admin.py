from django.contrib import admin
from .models import Property

class PropertyAdmin(admin.ModelAdmin):
    # Поля, которые будут видны в списке всех объектов
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'property_type', 'rooms')
    # Поля-ссылки (на что можно нажать, чтобы войти в объект)
    list_display_links = ('id', 'title')
    # Фильтры справа
    list_filter = ('property_type', 'rooms', 'city')
    # Поля, которые можно редактировать прямо в списке
    list_editable = ('is_published',)
    # Поиск
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    # Кол-во объектов на странице
    list_per_page = 25

admin.site.register(Property, PropertyAdmin)