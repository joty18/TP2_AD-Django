from hospital.models import Utente
import django
from django.contrib.auth.models import Group
import csv

django.setup()

def run():

    f = open(r'C:\Users\Tiago\PycharmProjects\djangoProject\tp2\loads\utentes.txt', encoding="utf8")

    csvr = csv.reader(f, delimiter = ':')


    my_group = Group.objects.get(name='Utentes')

    for ut in csvr:
        try:
            bilhete_identidade = ut[1]
            u = Utente(nome=ut[0], bi=bilhete_identidade, NIF=ut[2], morada=ut[3],
                       codigo_postal=ut[4], username=ut[2])

            psw = ut[2]+'utente'
            u.set_password(psw)
            u.save()

            my_group.user_set.add(u)
        except:
            pass #ma pratica
