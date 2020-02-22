#!/usr/bin/env python

import random as rd


if __name__ == "__main__":

    print("Saisir le min :")
    rangeMin = int(input())

    print("Saisir le max :")
    rangeMax = int(input())

    print("règles du jeu : trouver le nombre entre " + str(rangeMin) + " et " + str(rangeMax))

    chosenNumber = rd.randint(rangeMin, rangeMax)
    typedNumber = rd.randint(rangeMin, rangeMax)

    while typedNumber != chosenNumber:
        print("Tapez :")
        typedNumber = int(input())
        if typedNumber > chosenNumber:
            print("c'est moins")
        elif typedNumber < chosenNumber:
            print("c'est plus")
        else :
            print("c'est gagné")
