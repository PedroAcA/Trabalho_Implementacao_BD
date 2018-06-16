from django.conf.urls import url

from . import views

urlpatterns = [
 #   url(r'^$', views.indice, name='indice'),
 	url(r'novo_partido/', views.novo_partido, name='novo_partido'),
 	url(r'lista_partido/',views.mostrar_partido, name='mostrar_partido'),
 	url(r'exclui_partido/',views.excluir_partido, name='excluir_partido'),
 	url(r'atualiza_partido/',views.atualizar_partido,name='atualizar_partido')
]