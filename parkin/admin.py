from django.contrib import admin
from .models import Car, Terminal, Zone, Supervisor

@admin.register(Car)
class ParkinAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date_start', 'date_end', 'terminal',)
    list_editable = ('terminal',)
    list_display_links = ('id', 'user', )

@admin.register(Terminal)
class TerminalAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'address',)
    list_display_links = ('id', 'number', )

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'street_start',)
    list_display_links = ('id',)


@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):
    list_display = ('id', 'zone',)
    list_display_links = ('id',)
