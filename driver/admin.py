from django.contrib import admin

from .models import driver, reservation


@admin.register(driver)
class driverAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'first_name',
        'last_name',
        'gender',
        'description_of_car',
        'address',
        'active',
        'birth_date',
        'car_id',
        'latitude',
        'longitude',
    )
    list_filter = ('user', 'active', 'birth_date')


@admin.register(reservation)
class reservationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'driver',
          'price',  
        'start_latitude',
        'start_longitude',
        'end_latitude',
        'end_longitude',
        'date',
      
    )
    list_filter = ('user', 'driver')