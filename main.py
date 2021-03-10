# Brief Retour sur la machine à groupes

#! /usr/bin/env python3
# coding: utf-8


if __name__ == "__main__":
    try:
        import fonctions
    except ModuleNotFoundError as e:
        print("Le package semble avoir disparu : ", e)
    else:
        print("ça marche")
        fonctions.main()
    finally:
        print("fin de la gestion des erreurs")

