#!/usr/bin/env python3
# -*- coding: utf-8 -*-

equivalences = {'I':1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M':1000}

def rom_to_dec(nombre_romain):
    """
    >>> rom_to_dec('I')
    1
    >>> rom_to_dec('II')
    2
    >>> rom_to_dec('IXX')
    19
    """
    if nombre_romain=='':
        return 0
    elif len(nombre_romain)==1:
        return equivalences[nombre_romain[0]]
    elif equivalences[nombre_romain[0]]>=equivalences[nombre_romain[1]]:#cas additif 
        return equivalences[nombre_romain[0]]+rom_to_dec(nombre_romain[1:])
    else :#cas soustractif 
        return rom_to_dec(nombre_romain[1:])-equivalences[nombre_romain[0]]
    
    
assert rom_to_dec('I') == 1
assert rom_to_dec('II') == 2