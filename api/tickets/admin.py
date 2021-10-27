from django.contrib import admin
from .models import Section, Rank, Seat


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'curved', 'balcony']


@admin.register(Rank)
class RanksAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'rank']


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['number', 'section', 'row', 'rank', 'user', 'blocked', 'is_aisle', 'is_front', 'is_balcony', 'is_available']