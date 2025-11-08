from django import forms
from .models import Voluntario

class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = ["nome", "email", "telefone", "endereco", "mensagem"]  
        widgets = {
            "nome": forms.TextInput(attrs={"placeholder": "Digite seu nome"}),
            "email": forms.EmailInput(attrs={"placeholder": "Digite seu e-mail"}),
            "telefone": forms.TextInput(attrs={"placeholder": "Digite seu telefone"}),
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
