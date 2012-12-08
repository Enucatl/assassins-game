#!/usr/bin/env python
#coding=utf-8

from __future__ import division, print_function
from templates import *
from send_email import SendEmail
import os

s = SendEmail()

class Assassin(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def send_email(self, subject, text):
        s.send(self.email, subject, text)

    def __repr__(self):
        return "('{0.name}', '{0.email}')".format(self)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name
        else:
            return False

class AssassinList(list):
    def __init__(self, *args, **kwargs):
        super(AssassinList, self).__init__(*args, **kwargs)

    def __delitem__(self, key):
        sub = next_target_sub
        msg = next_target_msg.substitute(
                name=self[key - 1].name,
                victim=self[key].name,
                next_target=self[(key + 1) % len(self)].name
                )
        self[key-1].send_email(sub, msg)
        super(AssassinList, self).__delitem__(key)

    def save(self, filename): 
        if os.path.exists(filename):
            print("attenzione, il file esiste già!")
            filename += ".bak"
        with open(filename, "w") as f:
            print(self, file=f)

    def load(self, filename):
        with open(filename) as f:
            loaded_list = eval(f.read())
            for name, email in loaded_list:
                self.append(Assassin(name, email))
