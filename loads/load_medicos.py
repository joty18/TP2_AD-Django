import http.client
import json
import csv

def get(conn, req):
    conn.request("GET", req)
    return conn.getresponse()

conn = http.client.HTTPConnection("127.0.0.1",8000)
headers = {'Content-type': 'application/json'}
f = open(r'C:\Users\user\Downloads\tp2ad\tp2ad\loads\medicos.csv', encoding='latin-1')
csvr = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_ALL)

for index, m in enumerate(csvr):
    md = {
            'username': 'medico'+str(index),
            'password': 'a',
            'nome': m['Nome'],
            'bi': m['BI'],
            'NIF': m['NIF'],
            'morada': m['Morada'],
            'codigo_postal': m['Codigo postal'],
            'especialidade': m['Especialidade'],
            'cedula': m['Cedula']
        }
    conn.request("POST", '/medicos/', json.dumps(md), headers=headers)
    r = conn.getresponse()
    print(r.status, r.reason, r.read())