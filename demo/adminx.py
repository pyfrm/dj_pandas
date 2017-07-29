#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '29/07/2017'
__author__ = 'deling.ma'
"""

# coding=utf-8
import xadmin
from demo.models import TimeSeries, ComplexTimeSeries, MultiTimeSeries


@xadmin.sites.register(TimeSeries)
class TimeSeriesAdmin(object):
    list_display = ("id", "date", "value")


@xadmin.sites.register(MultiTimeSeries)
class MultiTimeSeriesAdmin(object):
    list_display = ("id", "series", "date", "value")


@xadmin.sites.register(ComplexTimeSeries)
class ComplexTimeSeriesAdmin(object):
    list_display = ("id", "site", "date", "value")

