#!/usr/bin/env python

import random as rd


def inputAndPrint(msg):
    print(msg)
    return int(input())


if __name__ == "__main__":

    rangeMin = inputAndPrint('Entrez le minimum :')

    rangeMax = inputAndPrint('Entrez le maximum :')

    print("règles du jeu : trouver le nombre entre " + str(rangeMin) + " et " + str(rangeMax))

    chosenNumber = rd.randint(rangeMin, rangeMax)
    typedNumber = rd.randint(rangeMin, rangeMax)

    while typedNumber != chosenNumber:
        typedNumber = inputAndPrint('Entrez un entier non nul :')
        if typedNumber > chosenNumber:
            print("c'est moins")
        elif typedNumber < chosenNumber:
            print("c'est plus")
        else:
            print("c'est gagné")
