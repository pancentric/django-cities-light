from __future__ import unicode_literals

from copy import copy

from django.contrib import admin
from django.contrib.admin.views.main import ChangeList

from .forms import *
from .models import *
from .settings import *


class CountryAdmin(admin.ModelAdmin):
    """
    ModelAdmin for Country.
    """

    list_display = (
        'name',
        'chinese_name',
        'code2',
        'code3',
        'continent',
        'tld',
        'active',
    )
    search_fields = (
        'name',
        'name_ascii',
        'code2',
        'code3',
        'tld'
    )
    list_filter = (
        'continent',
        'active',
    )
    form = CountryForm
admin.site.register(Country, CountryAdmin)


class RegionAdmin(admin.ModelAdmin):
    """
    ModelAdmin for Region.
    """
    list_filter = (
        'country__continent',
        'country',
    )
    search_fields = (
        'name',
        'name_ascii',
    )
    list_display = (
        'name',
        'chinese_name',
        'country',
        'active',
    )
    form = RegionForm
admin.site.register(Region, RegionAdmin)


class CityChangeList(ChangeList):
    def get_query_set(self, request):
        if 'q' in list(request.GET.keys()):
            request.GET = copy(request.GET)
            request.GET['q'] = to_search(request.GET['q'])
        return super(CityChangeList, self).get_query_set(request)


class CityAdmin(admin.ModelAdmin):
    """
    ModelAdmin for City.
    """
    list_display = (
        'name',
        'chinese_name',
        'region',
        'country',
        'active',
    )
    search_fields = (
        'search_names',
    )
    list_filter = (
        'country__continent',
        'active',
        'country',
    )
    #form = CityForm

    def get_changelist(self, request, **kwargs):
        return CityChangeList

admin.site.register(City, CityAdmin)
