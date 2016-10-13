#coding=utf-8

from django.contrib import admin
from .models import Pageview


class PageviewAdmin(admin.ModelAdmin):
    list_display = ('dtime','city','count','created_date')
    # search_fields = ('city', 'created_date')
    list_filter = ('dtime',)
    
    ordering = ('-dtime',)



admin.site.register(Pageview, PageviewAdmin)