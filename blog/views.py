from django.shortcuts import render, redirect
from blog.forms import MessageForm
from datetime import datetime
from django.views.generic import ListView
from .models import Message
from .forms import ContatoForm  # Certifique-se de ter o formulário adequado criado


def contato(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados no banco
            return redirect('home')  # Redireciona após o envio
    else:
        form = ContatoForm()
    return render(request, 'contato.html', {'form': form})






def log_message(request):
    form = MessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "message.html", {"form": form})



class HomeListView(ListView):
    """Renderiza a página inicial, com uma lista de todas as mensagens."""
    model = Message

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def sobre(request):
    return render(request, "sobre.html")



