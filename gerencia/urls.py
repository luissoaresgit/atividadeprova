from django.urls import path
from .views import inicio_gerencia, listagem_noticia, cadastrar_noticia, editar_noticia, categoria_listagem, categoria_cadastro, categoria_editar, categoria_remover

app_name = 'gerencia'

urlpatterns = [
    path('', inicio_gerencia, name='gerencia_inicial'),
    path('noticias/', listagem_noticia, name='listagem_noticia'),
    path('noticias/cadastro', cadastrar_noticia, name='cadastro_noticia'),
    path('noticias/editar/<int:id>', editar_noticia, name='editar_noticia'),
    # Add your URL patterns here
    path('categorias/', categoria_listagem, name='categoria_listagem'),
    path('categorias/cadastro/', categoria_cadastro, name='categoria_cadastro'),
    path('categorias/editar/<int:id>', categoria_editar, name='editar_categoria'),
    path('categorias/remover/<int:id>', categoria_remover, name='remover_categoria'),
]