from django.contrib import admin
from .models import *


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'shirt_size')
    list_display_links = ('id', 'name', 'shirt_size')
    search_fields = ('name', 'shirt_size')


class RunnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'MedalType', 'medal')
    list_display_links = ('id', 'name', 'MedalType', 'medal')
    # search_fields = ('name',)


admin.site.register(Person, PersonAdmin)
admin.site.register(Runner, RunnerAdmin)


admin.site.site_title = 'Админ-панель "Изучение Django"'
admin.site.site_header = 'Админ-панель "Изучение Django"'
