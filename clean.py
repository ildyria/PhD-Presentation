#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import errno
import sys

def save(fn,z):
  d = open(fn,'w')
  d.write(z)
  d.close()

def load(fn):
  d = open(fn,'r')
  z = d.read()
  d.close()
  return z


def tryload(fn):
  try:
    return load(fn)
  except IOError as e:
    if e.errno in [errno.ENOENT,errno.ENAMETOOLONG]:
      return None
    raise

def main():
    output = ''
    skip = False;
    for f in load('results-aead.html').split('\n'):

        if "forgery" in f:
            skip = True
            continue
        if "decrypt" in f:
            skip = True
            continue
        if "long+long" in f :
            skip = True
            continue
        if "0+long" in f :
            skip = True
            continue
        if "1536" in f :
            skip = True
            continue
        if "64+0" in f :
            skip = True
            continue
        if "0+64" in f :
            skip = True
            continue
        if "64+64" in f :
            skip = True
            continue
        if "table" in f:
            skip = False
        if skip:
            continue
        if "pae" in f:
            continue
        if "aes" in f:
            continue
        if "whe" in f:
            continue
        if "acorn" in f:
            continue
        if "ascon" in f:
            continue
        if "ca" in f:
            continue
        if "artemia" in f:
            continue
        if "morus" in f:
            continue
        if "lacv1" in f:
            continue
        if "cm" in f:
            continue
        if "scr" in f:
            continue
        if "twi" in f:
            continue
        if "sha" in f:
            continue
        if "tri" in f:
            continue
        if "pi16" in f:
            continue
        if "pi32" in f:
            continue
        if "pi64" in f:
            continue
        if "hs" in f:
            continue
        if "jol" in f:
            continue
        if "sab" in f:
            continue
        if "pro" in f:
            continue
        if "cba" in f:
            continue
        if "elm" in f:
            continue
        if "pres" in f:
            continue
        if "prima" in f:
            continue
        if "tia" in f:
            continue
        if "kia" in f:
            continue
        if "led80" in f:
            continue
        if "deo" in f:
            continue
        if "icepole" in f:
            continue
        if "mina" in f:
            continue
        if "aez" in f:
            continue
        if "colm" in f:
            continue
        if "raviyo" in f:
            continue
        if "silver" in f:
            continue
        if "aegis" in f:
            continue
        if "enchi" in f:
            continue
        output += f + '\n'

    save('results-aead.new.html',output)

main()
