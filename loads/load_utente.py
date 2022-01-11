import http.client
import json
import csv

from tp2.hospital.models import Utente


def get(conn, req):
    conn.request("GET", req)
    return conn.getresponse()

conn = http.client.HTTPConnection("127.0.0.1",8000)
headers = {'Content-type': 'application/json'}
f = open(r'C:\Users\user\Downloads\tp2\tp2\loads\utentes.csv', encoding='latin-1')
csvr = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_ALL)

for l in csvr:
        data = {
            Utente.nome: l['Nome'],
            Utente.bi: l['BI'],
            Utente.NIF: l['NIF'],
            Utente.morada: l['Morada'],
            Utente.codigo_postal: l['Codigo Postal']

        }
conn.request("POST", '/utentes/', json.dumps(data), headers=headers)
r = conn.getresponse()
print(r.status, r.reason, r.read())
