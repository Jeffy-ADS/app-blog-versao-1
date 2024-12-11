from django.db import models
from django.utils import timezone
from datetime import datetime

class Message(models.Model):
    mensagem = models.CharField(default="Mensagem",max_length=500)
    log_date = models.DateTimeField(default=datetime.now()) # Armazena a data e hora que a mensagem foi inserida

    def __str__(self): # Retorna uma representação em string de uma mensagem.
        date = timezone.localtime(self.log_date)
        return f"'{self.mensagem}' logged on {date.strftime('%A, %d %B, %Y at %X')}"



class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=15)
    mensagem = models.TextField(max_length=500)
    data_envio = models.DateTimeField(auto_now_add=True)
    log_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.nome} - {self.email}"


