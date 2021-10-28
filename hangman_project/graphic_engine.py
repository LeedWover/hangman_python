import winsound, os, sys, msvcrt, time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)



def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def listPrint(array):
    for i in range(0, len(array)):
        
        clearConsole()
        print(array[i])
        time.sleep(1)

def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        winsound.PlaySound(os.getcwd() + "\\typewriter.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(0.04)


def import_print(file):
    with open(os.getcwd() + file, "r", encoding="UTF-8") as f:
        lines=f.readlines()
        for i in lines:
            typewriter(i)
            time.sleep(1)
        inputResult = input('\nKowalsky: Készen állsz?[Y/N]').lower()
        if inputResult.lower() == 'Y':
            f.close()
        elif(inputResult.lower() == 'N'):
            quit()


def menu_starter(array):
   i=0
   winsound.PlaySound("007.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
   for i in range(len(array)):
        time.sleep(0.1)
        clearConsole()
        print(array[i])
        i += 1
   while 1:
      for i in range(17, len(array)):
        time.sleep(0.1)
        clearConsole()
        print(array[i])
      if msvcrt.kbhit():
	      if ord(msvcrt.getch()) == 13:
	         break


""" listPrint(reject)
listPrint(download)
listPrint(difficulty)
import_print("\\Game over.txt")
menu_starter(menu) """
