from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from admin_searchable_dropdown.filters import AutocompleteFilter

from .forms import *
from .models import *


# from .models import <modelos a serem geridos>
# basicamente tudo o que aparece para o admin ele pode criar medicamentos e assim
@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ['nome_medicamento', 'forma_farmaceutica', 'dosagem', 'estado_autorizacao', 'generico',
                    'titular_AIM',]
    #prepopulated_fields = {'slug': ('nome_medicamento',)}
    search_fields = ('nome_medicamento', 'titular_AIM')
    ordering = ('nome_medicamento',)

@admin.register(Outro_Artigo)
class OutroArtigoAdmin(admin.ModelAdmin):
    list_display = [ 'nome_artigo', 'fornecedor',]
    search_fields = ('nome_artigo', 'fornecedor')
    ordering = ('nome_artigo',)


class UtenteAdmin(UserAdmin):
    add_form = UtenteCreationForm
    search_fields = ('nome', 'NIF')
    ordering = ('nome',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
        ('Personal info', {'fields': ('nome', 'morada', 'NIF', 'bi', 'codigo_postal', 'groups',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'username', 'nome', 'morada', 'NIF', 'bi', 'codigo_postal', 'password1',
            'password2', 'groups')}
         ),
    )

class EnfermeiroAdmin(UserAdmin):
    add_form = EnfermeiroCreationForm
    search_fields = ('nome', 'NIF','especialidade')
    ordering = ('nome',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
        ('Personal info', {'fields': ('nome', 'morada', 'NIF', 'bi', 'codigo_postal','especialidade', 'groups',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'username', 'nome', 'morada', 'NIF', 'bi', 'codigo_postal', 'especialidade', 'password1',
            'password2', 'groups')}
         ),
    )

class MedicoAdmin(UserAdmin):
    add_form = MedicoCreationForm
    search_fields = ('nome', 'NIF','cedula','especialidade')
    ordering = ('nome',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
        ('Personal info', {'fields': ('nome', 'morada', 'NIF', 'bi', 'codigo_postal','cedula','especialidade', 'groups',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'username', 'nome', 'morada', 'NIF', 'bi', 'codigo_postal', 'cedula','especialidade', 'password1',
            'password2', 'groups')}
         ),
    )

class FarmaceuticoAdmin(UserAdmin):
    add_form = FarmaceuticoCreationForm
    search_fields = ('nome', 'NIF')
    ordering = ('nome',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
        ('Personal info', {'fields': ('nome', 'morada', 'NIF', 'bi', 'codigo_postal','groups',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'username', 'nome', 'morada', 'NIF', 'bi', 'codigo_postal', 'password1',
            'password2', 'groups')}
         ),
    )

@admin.register(Ato_Medico)
class AtoMedicoAdmin(admin.ModelAdmin):
    list_display = ['medico', 'utente', 'hora', 'quant_med', 'medicamento',
                    'quant_art', 'outro_artigo']
    search_fields = ('medico', 'utente')
    ordering = ('utente',)

@admin.register(Ato_Enfermagem)
class AtoEnfermagemAdmin(admin.ModelAdmin):
    list_display = ['enfermeiro', 'utente', 'hora', 'quant_med', 'medicamento',
                    'quant_art', 'outro_artigo']
    search_fields = ('enfermeiro', 'utente')
    ordering = ('utente',)


@admin.register(Ato_Farmaceutico)
class AtoFarmaceuticoAdmin(admin.ModelAdmin):
    list_display = ['farmaceutico', 'hora', 'quant_med', 'medicamento',
                    'quant_art', 'outro_artigo']
    search_fields = ['farmaceutico','medicamento', 'outro_artigo']
    ordering = ('farmaceutico',)





admin.site.register(Utente, UtenteAdmin)
admin.site.register(Enfermeiro, EnfermeiroAdmin)
admin.site.register(Medico,MedicoAdmin)
admin.site.register(Farmaceutico, FarmaceuticoAdmin)

