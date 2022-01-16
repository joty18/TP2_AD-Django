from django.urls import path
from . import views


app_name = 'hospital'
urlpatterns = [
    path('', views.log_in, name='login'),
    path('logout', views.log_out, name='logout'),
    path('menuutente', views.menu_utente, name='menuutente'),
    path('menuutente/agendamento', views.listar_agendamentos_u, name='agendamentosutente'),
]