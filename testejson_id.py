#!/usr/bin/env python
#teste de entrada de ids
import urllib.request, json, csv
print("Insira o id")
id = input()
with urllib.request.urlopen("http://api.bbce.com.br/produto/{0}/negocios".format(id)) as url:
    data = json.loads(url.read().decode())

c_negocio = len(data['model'])
if c_negocio == 0:
    print("SEM negocios!")
else:
    print("COM negocios!")
    print("Nomei o arquivo")
    arquivo = input()
    output = csv.writer(open("{0}.csv".format(arquivo), "w"))

    negocio_headers = data['model'][0]
    keys = negocio_headers.keys()
    output.writerow(keys)

    i = 0
    while c_negocio > i:
        output.writerow(data['model'][i].values())
        i = i + 1
