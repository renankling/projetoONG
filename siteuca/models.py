# siteuca/models.py
from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator


telefone_validator = RegexValidator(
    regex=r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$',
    message="Digite um telefone válido. Ex: (21) 98765-4321"
)


nome_validator = RegexValidator(
    regex=r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$',
    message="O nome deve conter apenas letras e espaços."
)

class Projeto(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Integrante(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name="integrantes")
    nome = models.CharField(max_length=120)
    funcao = models.CharField(max_length=120)
    imagem = models.ImageField(upload_to="integrantes/")
    descricao = models.TextField(blank=True)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class Noticia(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name="noticias")
    titulo = models.CharField(max_length=180)
    conteudo = models.TextField(blank=True)
    data_publicacao = models.DateTimeField(auto_now_add=False)
    imagem = models.ImageField(upload_to="noticias/")
    link_externo = models.URLField()  
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo


class Voluntario(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name="voluntarios")
    nome = models.CharField(max_length=120)
    email = models.EmailField(max_length=100,blank=False)
    telefone = models.CharField(max_length=15, blank=False, validators=[telefone_validator])
    endereco = models.CharField(max_length=255, blank=False) 
    mensagem = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.nome} ({self.email})"

class Trilha(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name="trilhas")
    titulo = models.CharField(max_length=180)
    data_publicacao = models.DateTimeField(auto_now_add=False)
    imagem = models.ImageField(upload_to="trilhas/")
    link_externo = models.URLField()  
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.titulo