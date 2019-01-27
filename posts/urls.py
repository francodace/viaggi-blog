from django.conf.urls import url
from . import views as posts_views
from django.views.generic import ListView, DetailView
from .models import Post

# Lista dei post Home Page del Blog
# Post singoli del Blog
# Sezione Contatti

urlpatterns = [
    url(r'^$', ListView.as_view(
        queryset = Post.objects.all().order_by("-data"),
        template_name = "lista_post.html",
        paginate_by = 5), name = "lista"),

    url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', DetailView.as_view(
        model = Post,
        template_name = "post_singolo.html"), name = "singolo"),

    url(r'^contatti/$', posts_views.contatti, name = "contatti"),
]
