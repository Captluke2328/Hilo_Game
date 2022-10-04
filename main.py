"""
Author : Lukas Johnny
Subject : CSE 210 - Programming With Classes Blocks
Project Title : Hilo Game
File : main.py
Date : 04-October-2022

Description : This is main script of this project that consist of parameters intialization that are needed to run the function script.

"""

import random as r
from function import *

class main:
    def __init__(self):
        self.orig_score = 300
        self.wins_score = 100
        self.lost_score = 75
        self.individual_card = 9
        self.function = function(self)
        
    def card(self):
        while True:
            self.next_card = r.randint(1,13)
            self.score = self.function.display(self.next_card)
            
            user_guess = input("Play again ? [y/n] : ")
            
            if user_guess == "n":
                break
            
            if self.function.getscore() <=0:
                print(f"************ GAME OVER *******************")
                break
            
            else:
                continue

if __name__ == "__main__":  
    init = main()
    init.card()
        


    