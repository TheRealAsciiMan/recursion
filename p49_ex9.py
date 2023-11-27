#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def miroir(une_chaine):
    """
    Fonction qui renvoie en miroir une chaine de caracteres
    Pre-condition : Une_chaine, chaine de caracteres à inverser
    Post-condition : Retourne la chaine inversée
    >>> miroir('bons')
    'snob'    
    """
    chaine_miroir = ""
    for c in une_chaine :
        chaine_miroir = c + chaine_miroir
    return chaine_miroir

def miroir_recur(une_chaine):
    """
    Fonction qui renvoie en miroir une chaine de caracteres
    Pre-condition : Une_chaine, chaine de caracteres à inverser
    Post-condition : Retourne la chaine inversée
    >>> miroir_recur('bons')
    'snob'    
    """
    if len(une_chaine)==1:
        return une_chaine
    else :
        return une_chaine[-1] + miroir_recur(une_chaine[:-1])
    
def palindrome(une_chaine):
    """
    >>> palindrome('anna')
    True
    >>> palindrome('anne')
    False
    """
    return une_chaine==miroir_recur(une_chaine)
