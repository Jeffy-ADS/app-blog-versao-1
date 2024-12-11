from django.urls import path
from blog import views
from blog.models import Message

home_list_view = views.HomeListView.as_view( 
    queryset=Message.objects.order_by("-log_date")[:5], # :5 limita os resultados aos cinco mais recentes
    context_object_name="message_list",
    template_name="home.html",
)

urlpatterns = [
	path("", home_list_view, name="home"),
    path("sobre/", views.sobre, name="sobre"),
    path("contato/", views.contato, name="contato"),
    path("log/", views.log_message, name="log"),
]