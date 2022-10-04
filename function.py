"""
Author : Lukas Johnny
Subject : CSE 210 - Programming With Classes Blocks
Project Title : Hilo Game
File : function.py
Date : 04-October-2022

Description : This is function script of this project that read user input and execute the logic

"""

from main import *

class function:
    def __init__(self,data):
        self.orig = data.orig_score
        self.wins = data.wins_score
        self.lost   = data.lost_score
        self.current_card = data.individual_card
        self.score = self.orig
        self.point = []
       
    def display(self,next):
        
        self.next_card = next
         
        print(f"\n*************** HILO GAME *********************\n")        
        print(f"The card is   : {self.current_card}")            
        print(f"Your score is : {self.userInputCheck()}")     
        print(f"Next Card Was : {self.next_card}")
        
        if self.next_card != self.current_card:
            self.current_card = self.next_card   
        
        return self.userInputCheck
        
    def userInputCheck(self):
        
        self.user_guess = input("Higher or lower ? [h/l] : ")
        
        if self.user_guess == "h":
            if self.current_card  > self.next_card:
                self.score = self.score + self.wins
            
            elif self.current_card == self.next_card:
                self.score
                
            else:
                self.score = self.score - self.lost
                       
        elif self.user_guess == "l":
            if self.current_card  < self.next_card:
                self.score = self.score + self.wins
            
            elif self.current_card == self.next_card:
                self.score
            
            else:
                self.score = self.score - self.lost
                
        self.point.append(self.score)
        
        return self.score
    
    def getscore(self) ->str:
        return self.score
          