import sys
from wordle import initiatePuzzle
import os
from ascii import initA
from blackjack import startGame


def init():

    clear = lambda: os.system('cls')
    clear()

    print("Welcome to my Python Playground! I'm just learning things here, so feel free to input a keyword to try out one of my projects.")
    key = input("Valid Inputs: \"close\", \"wordle\", \"ascii\", \"blackjack\": ")


    PlaygroundKeys = ['wordle', 'ascii', 'blackjack']


    if key == "close":
        print('Exiting...')
        quit()
        
    if key == "wordle":
        clear = lambda: os.system('cls')
        clear()
        initiatePuzzle()

    if key == "ascii":
        input('To do this, connect DroidCam. Once you have finished, press enter to begin the webcam.')
        clear = lambda: os.system('cls')
        clear()
        initA()

    if key == 'blackjack':
        clear = lambda: os.system('cls')
        clear()
        startGame()

    if key not in PlaygroundKeys:
        print('You didn\'t input a valid playground key.')
        quit()

init()
