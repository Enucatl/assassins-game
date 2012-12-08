#!/usr/bin/env python
#coding=utf-8

from __future__ import division, print_function
from Assassin import * 
from random import shuffle
import sys
import os

print("python Kill.py assassins_dictionary old_log new_log")

assassins_dictionary = eval(open(sys.argv[1]).read())
l = AssassinList()
l.load(sys.argv[2])

ucciso = ''
while (ucciso != 'q'):
    ucciso = raw_input("Inserisci il nome del giocatore ucciso: ")
    try:
        i = l.index(Assassin(ucciso, assassins_dictionary[ucciso]))
    except KeyError:
        print("key not found")
        break
    del l[i]

l.save(sys.argv[3])
