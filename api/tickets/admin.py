from django.contrib import admin
from .models import Section, Row, Rank, Seat


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'curved', 'balcony']

@admin.register(Row)
class RowsAdmin(admin.ModelAdmin):
    list_display = ['id', 'row', 'section',]


@admin.register(Rank)
class RanksAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'rank', 'cost']


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['number', 'row', 'rank', 'is_aisle', 'is_front', 'is_balcony', 'is_available']