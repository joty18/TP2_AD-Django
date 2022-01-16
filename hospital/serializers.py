from rest_framework import serializers
from .models import *

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '_all_'

class OutroArtigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outro_Artigo
        fields = '_all_'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '_all_'

class UtenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utente
        fields = '_all_'

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '_all_'

class FarmaceuticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmaceutico
        fields = '_all_'

class EnfermeiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermeiro
        fields = '_all_'