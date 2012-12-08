#!/usr/bin/env python
#coding=utf-8

from __future__ import division, print_function
from string import Template

next_target_sub = "[Assassini] Prossima vittima"
next_target_msg = Template("""Caro $name,
          Congratulazioni! sei riuscito a uccidere $victim. Ma questo non
          basta. La tua vita e' appesa a un cucchiaio.
          Non avrai pace finche' non farai fuori $next_target.""")

start_game_sub = "[Assassini] Comincia il gioco!"
start_game_msg =  Template("""Caro $name,
          Comincia il gioco degli assassini! La tua prima vittima e' $next_target.
          Mostrami di cosa sei capace.""")
 
