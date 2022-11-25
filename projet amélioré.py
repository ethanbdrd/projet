# -*- coding: utf-8 -*-
from random import randint
from tkinter import *


class Att :
    def __init__ (self,nom):
        
        self.nom = nom
        self.energie = 50
        self.alive = True 
        
    def soigner(self):
        if self.alive == True:
            if self.energie + 10 > 50:
                self.energie = 50
            else :
                self.energie += 10
        
    def blesser(self):
        self.energie -= 15
        if self.energie <= 0:
            self.alive = False
            
    def att_spe(self):
        att_special = randint(0,20)
        self.energie -= att_special
        if self.energie <= 0:
            self.alive = False
            
    def soin_spe(self):
        if self.alive == True:
            soin_special = randint(0,20)
            if self.energie + soin_special > 50 :
                self.energie = 50
            else :
                self.energie += soin_special 
            
    def get_nom(self):
        return self.nom
    
    def get_energie(self):
        return self.energie
    
    def is_alive(self):
        return self.alive
    
    def __str__(self):
        return f"{self.nom},{self.energie},"
 
class Def :
    def __init__ (self,nom):
        
        self.nom = nom
        self.energie = 60
        self.alive = True 
        
    def soigner(self):
        if self.alive == True:
            if self.energie + 15 > 50:
                self.energie = 50
            else :
                self.energie += 15
        
    def blesser(self):
        self.energie -= 8
        if self.energie <= 0:
            self.alive = False
            
    def att_spe(self):
        att_special = randint(0,15)
        self.energie -= att_special
        if self.energie <= 0:
            self.alive = False
            
    def soin_spe(self):
        if self.alive == True:
            soin_special = randint(0,30)
            if self.energie + soin_special > 50 :
                self.energie = 50
            else :
                self.energie += soin_special 
            
    def get_nom(self):
        return self.nom
    
    def get_energie(self):
        return self.energie
    
    def is_alive(self):
        return self.alive
    
    def __str__(self):
        return f"{self.nom},{self.energie},"
a = input("comment s'appelle le perso de l'utilisateur 1 ?")
b = input("comment s'appelle le perso de l'utilisateur 2 ?")
at = ''
de = ''
choixclass1 = input("Quel type pour le J1? at : attaque, de : defense")
if choixclass1 == 'at' :
    player1 = Att(a)
if choixclass1 == 'de' :
    player1 = Def(a)
choixclass2 = input("Quel type pour le J2? at : attaque, de: defense")
if choixclass2 == 'at' : 
    player2 = Att(b)
if choixclass2 == 'de' : 
    player2 = Def(b) 
c = randint(1,2)
tour_1 = ''
tour_2 = ''
if c == 1:
    tour_1 = player1
    tour_2 = player2
    print('le joueur1 ',tour_1.get_nom(),'commence')
else:
    tour_1 = player2 
    tour_2 = player1
    print('le joueur2',tour_1.get_nom(),' commence')

while player1.is_alive() and player2.is_alive() == True:
    print()
    print('Le joueur1',player1.get_nom(),'a',player1.get_energie(),'dénergie et le joueur2',player2.get_nom(),'a',player2.get_energie(),'dénergie')
    print('Au tour de',tour_1.get_nom(),'!')
    root = Tk()
    bouton1 = Button(root, text='Attaque', width=20, command=tour_2.blesser())
    bouton1.pack(pady=10)
    bouton2 = Button(root, text='Defense', width=20, command=tour_1.soigner())
    bouton2.pack(pady=10)
    bouton3 = Button(root, text='Attaque spéciale', width=20, command=tour_2.att_spe())
    bouton3.pack(pady=10)
    bouton4 = Button(root, text='Défense spéciale', width=20, command=tour_1.soin_spe())
    bouton4.pack(pady=10)
    root.mainloop()

    print()
    if tour_2.is_alive() == True:
        print('Le joueur1',player1.get_nom(),'a',player1.get_energie(),'dénergie et le joueur2',player2.get_nom(),'a',player2.get_energie(),'dénergie')
        print('Au tour de',tour_2.get_nom(),'!')
        root = Tk()
        bouton5 = Button(root, text='Attaque', width=20, command=tour_1.blesser())
        bouton5.pack(pady=10)
        bouton6 = Button(root, text='Defense', width=20, command=tour_2.soigner())
        bouton6.pack(pady=10)
        bouton7 = Button(root, text='Attaque spéciale', width=20, command=tour_1.att_spe())
        bouton7.pack(pady=10)
        bouton8 = Button(root, text='Défense spéciale', width=20, command=tour_2.soin_spe())
        bouton8.pack(pady=10)
        root.mainloop()

        
if player1.is_alive() == False:
    print(player2.get_nom(),'gagne !')
if player2.is_alive() == False:
    print(player1.get_nom(),'gagne !')






