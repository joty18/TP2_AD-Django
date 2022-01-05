from django.urls import path
from . import views

app_name = 'hospital'
urlpatterns = [
    path('',views.all_medicamentos,name='all_medicamentos'),

]