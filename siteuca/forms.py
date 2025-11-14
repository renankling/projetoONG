from django import forms
from .models import Voluntario

class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = ["nome", "email", "telefone", "endereco", "mensagem"]  
        widgets = {
            "nome": forms.TextInput(attrs={"placeholder": "Digite seu nome", "pattern": r"[A-Za-zÀ-ÖØ-öø-ÿ\s]+", "title": "Digite apenas letras (A-Z) e espaços"}),
            "email": forms.EmailInput(attrs={"placeholder": "Digite seu e-mail","type": "email"}),
            "telefone": forms.TextInput(attrs={"placeholder": "Digite seu telefone", "pattern": r"\(?\d{2}\)?\s?\d{4,5}-?\d{4}", "title": "Digite um telefone válido, ex: (11) 98765-4321"}),
            "endereco": forms.TextInput(attrs={"placeholder": "Digite o nome da  rua"}),
            "mensagem": forms.Textarea(attrs={"placeholder": "Deixe uma mensagem", "rows": 4}),
        }
        labels = {
            "nome": "Nome",
            "email": "E-mail",
            "telefone": "Telefone",
            "endereco": "Endereço",
            "mensagem": "Mensagem",
        }
