from django.urls import path
from . import views

app_name = 'hospital'
urlpatterns = [
    path('',views.all_medicamentos,name='all_medicamentos'),
    path('',views.all_utentes,name='all_utentes'),
    path('',views.all_outroartigos,name='all_outroartigos'),
]