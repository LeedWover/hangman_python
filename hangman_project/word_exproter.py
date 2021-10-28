
import os
import random
from graphics import *
from graphic_engine import *


def selectDifficulty():
  dif_lvl = 0 
  while int(dif_lvl) == 0 or int(dif_lvl)>3:
    listPrint(difficulty)
    dif_lvl = input('Select a difficulty:[1:(Easy), 2:(Medium), 3:(Hard)]')
    print(dif_lvl)
    while dif_lvl != '1' and dif_lvl != '2' and dif_lvl != '3':
        dif_lvl = input('Bad format, select a difficulty:[1:(Easy), 2:(Medium), 3:(Hard)]')
    #os.system('cls' if os.name == 'nt' else 'clear')    
  return dif_lvl


def lives(dif_lvl):
    if dif_lvl == '1':
        return 6
    elif dif_lvl == '2':
        return 5
    elif dif_lvl == '3':
        return 4


def exporter(dif_lvl):

    with open("countries-and-capitals.txt",encoding="UTF-8") as f:
        contents = f.read().splitlines()
        cities = []
        easy = []
        medium = []
        hard = []

        for city in contents:
            cities.append(city.split("|")[1].strip())

        for city in cities:
            if len(city) < 5:
                easy.append(city)
            elif len(city) < 7:
                medium.append(city)
            elif len(city) < 12:
                hard.append(city)

        if dif_lvl == "1":
            return random.choice(easy)
        elif dif_lvl == "2":
            return random.choice(medium)
        elif dif_lvl == "3":
            return random.choice(hard)
        
