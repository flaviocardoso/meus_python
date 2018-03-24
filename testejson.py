#!/usr/bin/env python
import urllib.request, json, csv, time

init = time.time()

with urllib.request.urlopen("http://api.bbce.com.br/produto/todos") as url:
    data = json.loads(url.read().decode())
    #print(data["id"])

#lista = list(data[["id"]])
c_data = len(data)
#id = 1281
'''
for x in data :
    if x['id']==id:
        c = len(x['campos'])
        for key in x['campos'][0].keys():
            print("{0} ".format(key), end="")
        print()
        for i in range(c):
            for value in x['campos'][i].values():
                print("{0} ".format(value), end="")
            print()'''
#output = csv.writer(open("teste_id_desc.csv", "w"))
#output.writerow(data[0].keys())
#for row in data[0]:
#ent_headers = data[0]
#keys = list(ent_headers.keys())
#values = ent.values()
#output.writerow((keys[0], keys[1]))
"""for key in keys:
    print("{0} ".format(key), end="")
    output.writerow(keys)"""
i = 0
while c_data > i:
    #cont = list(data[i].values())
    #output.writerow((cont[0], cont[1]))
    print(data[i]['id'], data[i]['descricao'])
    i = i + 1
"""output.writerow(data[:].values())"""
"""for i in range(c_data):
    print(data[i].values())
    for value in data[i].values():
        print(value)
        #output.writerow(value)
    for row in data[i]:
        print(row)
        output.writerow(row)
        """
fim = time.time()
print("{0}".format(fim - init))
