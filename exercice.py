#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    nombre= float (input("Entrez un nombre: "))
    return abs(nombre)


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOPQ', 'ack'
    result=[]
    for letter in prefixes:
        result.append(letter + suffixes)

    return result


def prime_integer_summation() -> int:
    summation = 0
    
    for number in range(2,542) :
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            #print(number)
            summation += number
                
    return summation


def factorial(number: int) -> int:
    return 0


def use_continue() -> None:
    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombres entiers est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
