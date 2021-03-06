from django.contrib.auth.models import User, UserManager, AbstractUser
from django.db import models


class Utilizador(User):
    nome = models.CharField(max_length=200)
    bi = models.CharField(max_length=200, unique=True)
    NIF = models.CharField(max_length=200, unique=True)
    morada = models.CharField(max_length=200)
    codigo_postal = models.CharField(max_length=200)


    objects = UserManager()

class Medico(Utilizador):
    especialidade = models.CharField(max_length=200)
    cedula = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ('nome',)
    def _str_(self):
        return f"Nome : {self.nome}, bi : {self.bi}"

class Enfermeiro(Utilizador):
    especialidade = models.CharField(max_length=200)

    class Meta:
        ordering = ('nome',)
    def _str_(self):
        return f"Nome : {self.nome}, bi : {self.bi}"

class Farmaceutico(Utilizador):

    class Meta:
        ordering = ('nome',)
    def _str_(self):
        return f"Nome : {self.nome}, bi : {self.bi}"


class Utente(Utilizador):

    class Meta:
        ordering = ('nome',)
    def _str_(self):
        return f"Nome : {self.nome}, bi : {self.bi}"

class Medicamento(models.Model):
    dci = models.CharField(max_length=200)
    nome_medicamento = models.CharField(max_length=200)
    forma_farmaceutica = models.CharField(max_length=100)  # , choices= FormaFarmaceutica.choices)
    dosagem = models.CharField(max_length=200)
    estado_autorizacao = models.BooleanField()
    generico = models.BooleanField()
    titular_AIM = models.CharField(max_length=200) #isto devia ser foreign key mas temos de arrranjar um maneira de converter
    #titular_AIM = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, null=True)
    #slug = models.CharField(max_length=200)
    #stock = models.PositiveIntegerField(default=0)

    def _str_(self):
        return f"{self.dci} - {self.nome_medicamento}"

class Outro_Artigo(models.Model):
    nome_artigo = models.CharField(max_length=200)
    fornecedor = models.CharField(max_length=200)

    def _str_(self):
        return f"{self.nome_artigo} - {self.fornecedor}"

class Ato_Medico(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    hora = models.DateTimeField(auto_now=True)
    quant_med = models.CharField(max_length = 200)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.SET_NULL, null=True)
    quant_art = models.CharField(max_length=200)
    outro_artigo = models.ForeignKey(Outro_Artigo, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('hora',)

    def _str_(self):
        return f"M??dico : {self.medico.nome}, Utente : {self.utente.nome}, Hora : {self.hora}" \
               f", Medicamento : {self.quant_med, self.medicamento}, Outros Artigos : {self.quant_art, self.outro_artigo}"

class Ato_Enfermagem(models.Model):
    enfermeiro = models.ForeignKey(Enfermeiro, on_delete=models.CASCADE)
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    hora = models.DateTimeField(auto_now=True)
    quant_med = models.CharField(max_length=200)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.SET_NULL, null=True)
    quant_art = models.CharField(max_length=200)
    outro_artigo = models.ForeignKey(Outro_Artigo, on_delete=models.SET_NULL, null=True)

    def _str_(self):
        return f"M??dico : {self.enfermeiro.nome}, Utente : {self.utente.nome}, Hora : {self.hora}" \
               f", Medicamento : {self.quant_med, self.medicamento}, Outros Artigos : {self.quant_art, self.outro_artigo}"

class Ato_Farmaceutico(models.Model):
    farmaceutico = models.ForeignKey(Farmaceutico, on_delete=models.CASCADE)
    hora = models.DateTimeField(auto_now=True)
    quant_med = models.CharField(max_length=200)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.SET_NULL, null=True)
    quant_art = models.CharField(max_length=200)
    outro_artigo = models.ForeignKey(Outro_Artigo, on_delete=models.SET_NULL, null=True)

    def _str_(self):
        return f"M??dico : {self.farmaceutico.nome}, Hora : {self.hora}, Medicamento : {self.quant_med, self.medicamento}," \
               f"Outros Artigos : {self.quant_art, self.outro_artigo}"

class Stock_med(models.Model):
    id_med = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    quant = models.PositiveIntegerField()

class Stock_art(models.Model):
    id_art = models.ForeignKey(Outro_Artigo, on_delete=models.CASCADE)
    quant = models.PositiveIntegerField()