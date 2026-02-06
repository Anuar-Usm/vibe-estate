from django.db import models
from datetime import datetime

class Property(models.Model):
    # Основная информация
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    
    # Категории как на restproperty
    PROPERTY_TYPES = [
        ('Apartment', 'Квартира'),
        ('Villa', 'Вилла'),
        ('Penthouse', 'Пентхаус'),
        ('Commercial', 'Коммерческая'),
    ]
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES, default='Apartment')
    
    ROOM_PLANS = [
        ('1+0', 'Студия (1+0)'),
        ('1+1', '1+1'),
        ('2+1', '2+1'),
        ('3+1', '3+1'),
        ('4+1', '4+1'),
    ]
    rooms = models.CharField(max_length=50, choices=ROOM_PLANS, default='1+1')

    # Характеристики
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    distance_to_sea = models.IntegerField(null=True, blank=True, help_text="в метрах")
    
    # Фото (оставляем как было)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объект недвижимости"
        verbose_name_plural = "Объекты недвижимости"