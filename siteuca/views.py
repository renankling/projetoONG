# siteuca/views.py
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from .models import Noticia, Integrante, Voluntario, Projeto,Trilha
from .forms import VoluntarioForm

def home(request):
    projeto = Projeto.objects.first()
    trilhas = Trilha.objects.order_by('-data_publicacao')[:3]
    noticias = Noticia.objects.order_by('-data_publicacao')[:3]
    return render(request, "public/home.html", {
        "projeto": projeto, 
        "noticias": noticias,
        "trilhas": trilhas,
        })

class NoticiaListView(ListView):
    model = Noticia
    template_name = "public/noticias_list.html"
    context_object_name = "noticias"
    ordering = ["-data_publicacao"]


class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = "public/noticia_detail.html"
    context_object_name = "noticia"

class IntegranteListView(ListView):
    model = Integrante
    template_name = "public/integrantes.html"
    context_object_name = "integrantes"

class VoluntarioCreateView(CreateView):
    model = Voluntario
    form_class = VoluntarioForm
    template_name = "public/voluntario_form.html"
    success_url = reverse_lazy("voluntario_ok")
    def form_valid(self, form):
        projeto = Projeto.objects.first()
        if projeto is None:
            projeto = Projeto.objects.create(
                nome="Projeto Uçá",
                descricao="Projeto Uçá"
            )
        form.instance.projeto = projeto
        return super().form_valid(form)

class TrilhaListView(ListView):
    model = Trilha
    template_name = "public/trilhas.html"
    context_object_name = "trilhas"
    ordering = ["-data_publicacao"]


    def form_valid(self, form):
        projeto = Projeto.objects.first()
        if not projeto:
            projeto = Projeto.objects.create(nome="Uçá", descricao="Projeto Uçá")
        form.instance.projeto = projeto
        messages.success(self.request, "Recebemos seus dados. Obrigado por se voluntariar!")
        return super().form_valid(form)

from django.views.generic import TemplateView
class VoluntarioOKView(TemplateView):
    template_name = "public/voluntario_ok.html"


def is_staff(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_staff)
def dashboard(request):
    return render(request, "adminarea/dashboard.html", {
        "qtd_noticias": Noticia.objects.count(),
        "qtd_integrantes": Integrante.objects.count(),
        "qtd_voluntarios": Voluntario.objects.count(),
    })
