# siteuca/models.py
from django.conf import settings
from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Integrante(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name="integrantes")
    nome = models.CharField(max_length=120)
    funcao = models.CharField(max_length=120, blank=True)
    imagem = models.ImageField(upload_to="integrantes/", blank=True, null=True)
    descricao = models.TextField(blank=True)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class Noticia(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name="noticias")
    titulo = models.CharField(max_length=180)
    conteudo = models.TextField(blank=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to="noticias/", blank=True, null=True)
    link_externo = models.URLField(blank=True, null=True)  
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo


class Voluntario(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name="voluntarios")
    nome = models.CharField(max_length=120)
    email = models.EmailField(max_length=100,blank=False)
    telefone = models.CharField(max_length=30, blank=False)
    endereco = models.CharField(max_length=255, blank=False) 
    mensagem = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.nome} ({self.email})"
