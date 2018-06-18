from django.conf.urls import url
from views import views_partido 
from views import views_cargo 
from views import views_politico 
urlpatterns = [
 #   url(r'^$', views.indice, name='indice'),
 	#inicio das urls para crud de partido
 	url(r'novo_partido/', views_partido.novo_partido, name='novo_partido'),
 	url(r'lista_partido/',views_partido.mostrar_partido, name='mostrar_partido'),
 	url(r'exclui_partido/',views_partido.excluir_partido, name='excluir_partido'),
 	url(r'atualiza_partido/',views_partido.atualizar_partido,name='atualizar_partido'),
 	#fim das urls para crud de partido
 	
 	#inicio das urls para crud de cargo
 	url(r'novo_cargo/', views_cargo.novo_cargo, name='novo_cargo'),
 	url(r'lista_cargo/',views_cargo.mostrar_cargo, name='mostrar_cargo'),
 	url(r'exclui_cargo/',views_cargo.excluir_cargo, name='excluir_cargo'),
 	url(r'atualiza_cargo/',views_cargo.atualizar_cargo,name='atualizar_cargo'),
 	#fim das urls para crud de cargo

 	#inicio das urls para crud de politico
 	
 	url(r'novo_politico/', views_politico.novo_politico, name='novo_politico'),
 	url(r'lista_politico/',views_politico.mostrar_politico, name='mostrar_politico'),
 	url(r'exclui_politico/',views_politico.excluir_politico, name='excluir_politico'),
 	url(r'atualiza_politico/',views_politico.atualizar_politico,name='atualizar_politico'),
 	#fim das urls para crud de politico
]