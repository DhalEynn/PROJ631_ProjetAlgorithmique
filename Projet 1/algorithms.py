# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:39:15 2019

@author: Admin
"""

def princ (Astart, Astop, Hstart):
    print("1 - Foremost (arrive au plus tôt, peut importe le nombres d'arcs)")
    print("2 - Shortest (le plus court, en nombre d'arcs)")
    print("3 - Fastest (le plus rapide, mais avec potentiellement plus d'arcs)")
    test = 0
    while (test < 1 or test > 3):
        test = input("What algorithm do you want to use ?\n")
        if (type(test) != int):
            print("\n   You did not input a number !\n")
    if (test == 1):
        foremost(Astart, Astop, Hstart)
    elif (test == 2):
        shortest(Astart, Astop, Hstart)
    else:
        fastest(Astart, Astop, Hstart)

def foremost (Astart, Astop, Hstart):
    print ("foremost")
    print (Astart, Astop, Hstart)

def shortest (Astart, Astop, Hstart):
    print ("shortest")
    print (Astart, Astop, Hstart)

def fastest (Astart, Astop, Hstart):
    print ("fastest")
    print (Astart, Astop, Hstart)