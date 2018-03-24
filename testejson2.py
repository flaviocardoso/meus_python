#!/usr/bin/env python
#controle json teste

import json, requests, time
init = time.time()

uri = "http://api.bbce.com.br/produto/todos"

r = requests.get(uri)
json = r.json()
c_data = len(json)
#print(len(r))
i = 0
while c_data > i:
    print(json[i]['id'], json[i]['descricao'])
    i = i + 1

fim = time.time()
print("{0}".format(fim - init))
