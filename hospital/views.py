from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from django.core.exceptions import ValidationError

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

class Stock_medViewSet(viewsets.ModelViewSet):
    queryset = Stock_med.objects.all()
    serializer_class = Stock_medSerializer
    permission_classes = [permissions.AllowAny]

class Stock_artViewSet(viewsets.ModelViewSet):
    queryset = Stock_art.objects.all()
    serializer_class = Stock_artSerializer
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
            if user in User.objects.filter(groups__name="Utentes"):
                login(request, user)
                return HttpResponseRedirect('menuutente')
            elif user.is_superuser:
                login(request, user)
                return HttpResponseRedirect('/admin')
            else:
                raise ValidationError('Invalid user')

    return render(request, "login.html", {'form':form})
#-----------------------------------------------------------------------------------------------------------------------
#-----------------Utente--------------------------

@login_required(login_url='/hospital')
def menu_utente(request):
    return render(request, "menuutente.html", {})


@login_required(login_url='/hospital')
def listar_agendamentos_u(request):
    if request.method == "GET":
        u = request.user  # Não estou a ter em atenção se o utilizador é ou não médico; ou vai estar bloqueado/ ou tenho que pôr um if qualquer
        utente = Utente.objects.get(username=u)
        a= Ato_Medico.objects.all().filter(utente=utente).order_by('hora')
        agenda = [{"Medico":item.medico.nome, "Hora":item.datetime} for item in a]

        context={"agenda": agenda}

        return render(request, "agendamentosutente.html", context)



#-----------------------------TESTE-------------------------------------------------------------------------------------


@login_required(login_url='/hospital')
def adiciona_medicoes(request):
    form = FormStock_med(request.POST or None)
    if form.is_valid():
        Stock_med.quant-
        form.save()
        messages.success(request, "Medição registada com sucesso.")
    return render(request, "adicionamedicoes.html", {"form": form})
