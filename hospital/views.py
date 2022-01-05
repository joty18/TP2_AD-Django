from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MedicamentoSerializer
from .models import *

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    permission_classes = [permissions.AllowAny]