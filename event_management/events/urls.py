from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('evento/<int:evento_id>/', views.detalhe_evento, name='detalhe_evento'),
    path('criar/', views.criar_evento, name='criar_evento'),
    path('editar/<int:evento_id>/', views.editar_evento, name='editar_evento'),
    path('excluir/<int:evento_id>/', views.excluir_evento, name='excluir_evento'),
]
