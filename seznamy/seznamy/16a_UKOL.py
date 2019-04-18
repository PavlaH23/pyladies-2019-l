#!/usr/bin/env python3

# Mate seznam retezcu krestnich jmen
# zaznamy = ['pepa', 'Jiří', 'Ivo', 'jan']

# Nektera jmena zacinaji velkym a jine malym pismenem.

# 1. Napiste funkci ktera vrati seznam prvku, ktere zacinaji malym pismenem
# 2. Napiste funkci ktera vrati seznam prvku, ktere zacinaji velkym pismenem

# napr. vrat_mala_pismena(['pepa', 'Jiří', 'Ivo', 'jan']) => ['pepa', 'jan']
# napr. vrat_velka_pismena(['pepa', 'Jiří', 'Ivo', 'jan']) => ['Jiří', 'Ivo']

# Muzete pouzit funkci retezec.islower() na prvni pismeno retezce




def vrat_mala_pismena(jmena):
    vysledek = []
    for jmeno in jmena:
        if jmeno[0].islower():
            vysledek.append(jmeno)
    return vysledek


def vrat_velka_pismena(jmena):
    vysledek = []
    for jmeno in jmena:
        if jmeno[0].isupper():
            vysledek.append(jmeno)
    return vysledek

print(vrat_mala_pismena(['pepa', 'Jiří', 'Ivo', 'jan']))
print(vrat_velka_pismena(['pepa', 'Jiří', 'Ivo', 'jan']))
