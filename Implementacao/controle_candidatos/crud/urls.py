from django.conf.urls import url

from . import views

urlpatterns = [
 #   url(r'^$', views.indice, name='indice'),
 	#inicio das urls para crud de partido
 	url(r'novo_partido/', views.novo_partido, name='novo_partido'),
 	url(r'lista_partido/',views.mostrar_partido, name='mostrar_partido'),
 	url(r'exclui_partido/',views.excluir_partido, name='excluir_partido'),
 	url(r'atualiza_partido/',views.atualizar_partido,name='atualizar_partido'),
 	#fim das urls para crud de partido
 	#inicio das urls para crud de cargo
 	url(r'novo_cargo/', views.novo_cargo, name='novo_cargo'),
 	url(r'lista_cargo/',views.mostrar_cargo, name='mostrar_cargo'),
 	url(r'exclui_cargo/',views.excluir_cargo, name='excluir_cargo'),
 	url(r'atualiza_cargo/',views.atualizar_cargo,name='atualizar_cargo'),
 	#fim das urls para crud de cargo
]