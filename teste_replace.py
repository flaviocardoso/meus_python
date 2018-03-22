#!/usr/bin/env python
#teste de replace em python

q = "Seu nome é?"

mens = input(q)

print(q.replace("?", " {0}".format(mens)))
