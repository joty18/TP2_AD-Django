import http.client
import json
import csv

def get(conn, req):
    conn.request("GET", req)
    return conn.getresponse()

conn = http.client.HTTPConnection("127.0.0.1",8000)
headers = {'Content-type': 'application/json'}
f = open(r'C:\Users\Tiago\PycharmProjects\djangoProject\tp2\loads\utentes.csv', encoding='latin-1')
csvr = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_ALL)

for index,u in enumerate(csvr):
    ut = {
            'username': 'user'+str(index),
            'password': 'a',
            'nome': u['Nome'],
            'bi': u['BI'],
            'NIF': u['NIF'],
            'morada': u['Morada'],
            'codigo_postal': u['Codigo postal']
        }
    conn.request("POST", '/utentes/', json.dumps(ut), headers=headers)
    r = conn.getresponse()
    print(r.status, r.reason, r.read())