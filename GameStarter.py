#!/usr/bin/env python
#coding=utf-8

from __future__ import division, print_function
from Assassin import * 
from random import shuffle
import sys

print("Comincia il gioco degli assassini!")

assassins_dictionary = eval(open(sys.argv[1]).read())
l = AssassinList()
shuffled_list = assassins_dictionary.keys()
shuffle(shuffled_list)
for name in shuffled_list:
    l.append(Assassin(name, assassins_dictionary[name]))


for i in range(len(l)):
    l[i].send_email(start_game_sub,
            start_game_msg.substitute(name=l[i].name,
                next_target=l[(i + 1) % len(l)].name))

l.save(sys.argv[2])
