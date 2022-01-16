from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .forms import *
from .serializers import *
from .models import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    permission_classes = [permissions.AllowAny]

class OutroArtigoViewSet(viewsets.ModelViewSet):
    queryset = Outro_Artigo.objects.all()
    serializer_class = OutroArtigoSerializer
    permission_classes = [permissions.AllowAny]

class UtenteViewSet(viewsets.ModelViewSet):
    queryset = Utente.objects.all()
    serializer_class = UtenteSerializer
    permission_classes = [permissions.AllowAny]

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    permission_classes = [permissions.AllowAny]

class FarmaceuticoViewSet(viewsets.ModelViewSet):
    queryset = Farmaceutico.objects.all()
    serializer_class = FarmaceuticoSerializer
    permission_classes = [permissions.AllowAny]

class EnfermeiroViewSet(viewsets.ModelViewSet):
    queryset = Enfermeiro.objects.all()
    serializer_class = EnfermeiroSerializer
    permission_classes = [permissions.AllowAny]

#-----------------------------------------------------------------------------------------------------------------------


def log_out(request):
    logout(request)
    form = LoginForm(request.POST or None)
    m="Logout efetuado."
    return render(request, "login.html", {'form':form,'logout':m})


def log_in(request):

    form = LoginForm(request.POST or None)
    if form.is_valid():
        password = form.cleaned_data.get('password')
        username = form.cleaned_data.get('username')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user in User.objects.filter(groups__name="Funcionários"):
                login(request, user)
                return HttpResponseRedirect('menufuncionario')
            elif user in User.objects.filter(groups__name="Utentes"):
                login(request, user)
                return HttpResponseRedirect('menuutente')
            elif user in User.objects.filter(groups__name="Médicos"):
                login(request, user)
                return HttpResponseRedirect('menumedico')
            elif user.is_superuser:
                login(request, user)
                return HttpResponseRedirect('/admin')
            else:
                raise ValidationError('Invalid user')

    return render(request, "login.html", {'form':form})