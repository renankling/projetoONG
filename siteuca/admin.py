
from django.contrib import admin
from .models import Projeto, Integrante, Noticia, Voluntario

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("nome",)

@admin.register(Integrante)
class IntegranteAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "funcao", "projeto", "criado_por")
    search_fields = ("nome", "funcao")
    list_filter = ("projeto",)

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "projeto", "data_publicacao", "link_externo")
    search_fields = ("titulo",)
    list_filter = ("projeto",)
    fieldsets = (
        ("Conteúdo", {"fields": ("titulo", "conteudo", "imagem", "link_externo")}),
        ("Relacionamentos", {"fields": ("projeto", "autor")}),
    )

@admin.register(Voluntario)
class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "email", "projeto", "criado_em")
    search_fields = ("nome", "email")
    list_filter = ("projeto",)
