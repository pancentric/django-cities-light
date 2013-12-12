from __future__ import unicode_literals

from django import forms

from .models import Country, Region, City

__all__ = ['CountryForm', 'RegionForm', 'CityForm']


class CountryForm(forms.ModelForm):
    """
    Country model form.
    """
    class Meta:
        model = Country
        fields = ('name', 'chinese_name', 'continent', 'alternate_names')


class RegionForm(forms.ModelForm):
    """
    Region model form.
    """
    class Meta:
        model = Region
        fields = ('name', 'chinese_name', 'country', 'alternate_names')


class CityForm(forms.ModelForm):
    """
    City model form.
    """
    class Meta:
        model = City
        fields = ('name', 'chinese_name', 'region', 'country', 'alternate_names')
