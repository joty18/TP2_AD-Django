
import http.client
import json
import csv
from .models import *

def get(conn, req):
    conn.request("GET", req)
    return conn.getresponse()

conn = http.client.HTTPConnection("127.0.0.1",8000)

    conn.request("POST", '/stock/', json.dumps(data))
    r = conn.getresponse()
    print(r.status, r.reason, r.read())
