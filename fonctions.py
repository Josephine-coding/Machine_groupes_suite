#! /usr/bin/env python3
# coding: utf-8

import numpy as np
import os
import json
import random
historyGroup = []
groups = []

# Set up du décorateur @autotest
import doctest
import copy
import functools

def autotest(func):
    globs = copy.copy(globals())
    globs.update({func.name: func})
    doctest.run_docstring_examples(
        func, globs, verbose=True, name=func.name)
    return func

# Classe Apprenant
class Apprenant:
    def __init__(self, name, skill=0):  # Renseigner obligatoirement et name, skill est optionel
        self.name = name
        self.skill = np.random.choice(5)
        self.link = []
        self.learners = {}
        for x in promo.getMember():
            self.newLearner(x.name)
            x.newLearner(name)
        promo.addMember(self)

    def removeLearner(self, value):
        self.learners.pop(value)

    def setName(self, value):
        for x in promo.getMember():
            for nameLearner in x.learners:
                if nameLearner == self.name:
                    x.newLearner(value, x.learners[nameLearner])
                    x.removeLearner(self.name)
        self.name = value

    def setSkill(self, value):
        self.skill = value

    def newLearner(self, new, history=0):
        self.learners[new] = history

# Classe Promo
class Promo:
    def __init__(self):
        self.member = []

    def addMember(self, learner):
        self.member.append(learner)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def getMember(self):
        return self.member


promo = Promo()
listdir = os.listdir('./')
exist = False
for x in listdir:
    if x == 'promo.json':
        exist = True

if not exist:
    file = open('./promo.json', 'x')
    with open('./promo.json', 'w') as file:
        file.write(promo.toJSON())

with open('./promo.json', 'r') as file:
    promo_data = json.load(file)

# Liste des apprenants
Apprenant("Antoine Dewynter")
Apprenant("ArthurT")
Apprenant("CamilleS")
Apprenant("Farid Berrabah")
Apprenant("Giovanny M")
Apprenant("Joséphine")
Apprenant("Julien Vansteenkiste")
Apprenant("Kevin Faby")
Apprenant("Marie De smedt")
Apprenant("Mickael Fayeulle")
Apprenant("Phichet")
Apprenant("Rachid K.")
Apprenant("Tanguy Meyer")
Apprenant("Valentin Mineo")
Apprenant("vivien")
Apprenant("kevinb")
Apprenant("Hatice")

# Fonction pour ajouter des apprenants
def addLearner():
    newstudent = {}
    print('Enter the new name:')
    name = input()
    dontAdd = True
    while dontAdd :
        dontAdd = False
        for x in promo.getMember() :
            if x.name.lower() == name.lower() :
                dontAdd = True
                print(name, ' is already in the promo, please chose a new name :')
                name = input()
    Apprenant(name)

# Edition d'un apprenant
def edit():
    for x in promo.getMember():
        print(x.name)

    print("\nSelect learner : ")
    learner = input().lower()

    for x in promo.getMember():
        if x.name.lower() == learner:
            learner = x
            break

    print(learner.name, learner.skill, sep=" ")
    print("1: edit name\n2: edit skill")
    nb = input()

    if nb == '1':
        print("enter new name")
        new = input()
        learner.setName(new)
    elif nb == '2':
        print("enter new skill level")
        new = input()
        learner.setSkill(int(new))
    else:
        pass

    print(learner.name, learner.skill, sep=" ")
    print("Done\n")


# Print learner
def printLearners() :
    for x in promo.getMember():
        print(x.name, x.skill, "\n", x.learners, "\n")

# Remove learner
def removeLearner() :
    printLearners()
    print("Select name :")
    name = input()
    for i, x in enumerate(promo.getMember()) :
        if x.name.lower() == name.lower() :
            promo.getMember().pop(i)
            break
    for x in promo.getMember() :
        x.removeLearner(name)


# Help
def helps():
    print("help   : print available commands") # OK
    print("add    : add new learner") # OK
    print("edit   : edit learner") #OK
    print("create history : create new group with history") #OK
    print("create comp : create new group")
    print("show   : Show groups") #OK
    print("print  : Print learners") #OK
    print("remove : Remove learners") #OK
    print("quit   : exit programm") # OK
    print("history: Show group history") # Ok
    print("")


# Création des groupes
def getGroups(group_size, sort_by=None):
    copy_promo = list(promo.getMember())
    if sort_by == 3 or sort_by == 2:
        copy_promo.sort(key=lambda user: user.skill)
    else:
        random.shuffle(copy_promo)
    groups = np.array_split(np.asarray(copy_promo), round(len(promo.getMember()) / group_size))

    if sort_by == 2:
        groups_size = [len(group) for group in groups]
        groups = []
        for group_size in groups_size:
            coeff = round(len(copy_promo) / group_size)
            group = []
            for i in range(group_size):
                position = (coeff * i) - i
                group.append(copy_promo[position])
                copy_promo.pop(position)
            groups.append(group)
    return groups


def getHistoryGroup(size=2):
    if size >= len(promo.getMember()) / 2:
        size = len(promo.getMember()) // 2
    nb_group = len(promo.getMember()) // size
    rest = len(promo.getMember()) % size
    tmp = promo.getMember().copy()

    groups = []
    for i in range(nb_group):
        groups.append([])

    for group in groups:
        indexLearner = np.random.choice(len(tmp))
        learner = tmp[indexLearner]
        group.append(learner)
        tmp.remove(learner)

    grp = 0
    while len(tmp) > 0:
        getMembers(groups[grp], tmp)
        if grp >= nb_group - 1:
            grp = 0
        else:
            grp = grp + 1

    return groups


def getMembers(group, tmp):
    candidat = []
    listName = []
    saveName = None
    saveValue = -1

    for x in tmp:
        listName.append(x.name)

    for x in group:
        candidat.append(x.learners.items())

    for name in listName:
        tmpValue = 0
        for memberList in candidat:
            for member in memberList:
                if member[0] == name:
                    tmpValue += member[1]
        if tmpValue < saveValue or saveValue == -1:
            saveValue = tmpValue
            saveName = name

    for learner in tmp:
        if learner.name == saveName:
            group.append(learner)
            tmp.remove(learner)


# Save Groups
def saveGroups(groups) :
    for group in groups :
        members = []
        for learner in group :
            members.append(learner.name)
        for learner in group :
            for m in members :
                if m != learner.name :
                    learner.learners[m] = learner.learners[m] + 1
    historyGroup.append(groups)

# Print Groups
def printGroups(groups) :
    for i, group in enumerate(groups) :
        learners = ""
        for learner in group :
            learners += learner.name + ", "
        print("groupe " + str(i) + " : " + str(learners))


def main():
    # Ici on doit mettre toutes les instructions lancées dans le fichier

    run = True
    groups = []

    print("Welcome in group generator 0.1\nsend help to see our commands !\nHave fun\n")

    while run:
        inp = input().lower()

        if inp == 'quit':
            print("bye")
            run = False
        elif inp == "help":
            helps()
        elif inp == "edit":
            edit()
        elif inp == "print":
            printLearners()
        elif inp == "remove":
            removeLearner()
        elif inp == "add":
            addLearner()
        elif inp == "create comp":
            print("group size :")
            size = input()
            print("add filtre : \n1: none\n2 : Heterogene\n3 : Homogene")
            filtre = input()
            groups = getGroups(int(size), int(filtre))
            printGroups(groups)
            print("save groups ? (Y/N)")
            rep = input().lower()
            if rep == 'y':
                saveGroups(groups)
                historyGroup.append(groups)
                print("group saved\n")
        elif inp == "create history":
            print("enter group size :")
            size = input()
            groups = getHistoryGroup(int(size))
            printGroups(groups)
            print("save groups ? (Y/N)")
            rep = input().lower()
            if rep == 'y':
                saveGroups(groups)
                historyGroup.append(groups)
                print("group saved\n")
            else:
                groups = []
        elif inp == "show":
            printGroups(groups)
        else:
            pass


if __name__ == "__main__":
    main()