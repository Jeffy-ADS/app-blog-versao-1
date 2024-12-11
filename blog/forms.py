from django import forms
from blog.models import Contato, Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("mensagem",)   # NOTE: a vírgula final é obrigatória.


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone', 'mensagem']

