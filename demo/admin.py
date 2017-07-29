# coding=utf-8
from django.contrib import admin

from demo.models import TimeSeries, ComplexTimeSeries, MultiTimeSeries


class TimeSeriesAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "value")

admin.site.register(TimeSeries, TimeSeriesAdmin)


class MultiTimeSeriesAdmin(admin.ModelAdmin):
    list_display = ("id", "series", "date", "value")

admin.site.register(MultiTimeSeries, MultiTimeSeriesAdmin)


class ComplexTimeSeriesAdmin(admin.ModelAdmin):
    list_display = ("id", "site", "date", "value")

admin.site.register(ComplexTimeSeries, ComplexTimeSeriesAdmin)
