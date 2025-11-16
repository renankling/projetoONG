
from django.contrib import admin
from .models import Projeto, Integrante, Noticia, Voluntario, Trilha

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("nome",)

@admin.register(Integrante)
class IntegranteAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "funcao", "projeto", "criado_por")
    search_fields = ("nome", "funcao")
    list_filter = ("projeto",)
    exclude = ('criado_por',)

    def save_model(self, request, obj, form, change):
        if not obj.criado_por:
            obj.criado_por = request.user
        obj.save()

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "projeto", "data_publicacao", "link_externo", "criado_por")
    search_fields = ("titulo",)
    list_filter = ("projeto", "criado_por")
    exclude = ("criado_por",)

    def save_model(self, request, obj, form, change):
        if not obj.criado_por:
            obj.criado_por = request.user
        obj.save()

@admin.register(Voluntario)
class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "email", "projeto", "criado_em")
    search_fields = ("nome", "email")
    list_filter = ("projeto",)

@admin.register(Trilha)
class TrilhasAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "projeto", "data_publicacao", "criado_por")
    search_fields = ("titulo", "projeto__nome")
    list_filter = ("projeto", "data_publicacao")
    ordering = ("-data_publicacao",)
    date_hierarchy = "data_publicacao"
    exclude = ("criado_por",)

    def save_model(self, request, obj, form, change):
        if not obj.criado_por:
            obj.criado_por = request.user
        obj.save()