# -*- coding: utf-8 -*-
from random import randint

class Att :                         #Classe attaque qui a moins de vie mais qui se fais infliger plus de degat
    def __init__ (self,nom):
            
        self.nom = nom                  #nom
        self.energie = 50               #energie de base
        self.alive = True               #verifier si le perso est en vie
        
    def soigner(self):                  #methode soigner qui ajoute 10 à l'energie et qui peut aller au max à 50
        if self.alive == True:
            if self.energie + 10 > 50:
                self.energie = 50
            else :
                self.energie += 10
        
    def blesser(self):                  #methode blesser qui definit ce que le perso se fait infliger
        self.energie -= 8
        if self.energie <= 0:
            self.alive = False
            
    def att_spe(self):                  #attaque speciale qui tire un retourne une attaque allant de 0 à 15
        att_special = randint(0,15)
        self.energie -= att_special
        if self.energie <= 0:
            self.alive = False
            
    def soin_spe(self):                 #idem mais pour le soin
        if self.alive == True:
            soin_special = randint(0,20)
            if self.energie + soin_special > 50 :
                self.energie = 50
            else :
                self.energie += soin_special 
            
    def get_nom(self):                  #acceder au nom
        return self.nom
    
    def get_energie(self):              #acceder a l'énergie
        return self.energie
    
    def is_alive(self):                 #Booleen pour savoir si  le perso est en vie ou non
        return self.alive
    
    def __str__(self):                  #affichage propre
        return f"{self.nom},{self.energie},"
 
class Def :                             #Classe defense avec les meme methode mais avec des valeurs différentes pour creer des stratégies
    def __init__ (self,nom):
        
        self.nom = nom                  #meme principe
        self.energie = 60
        self.alive = True 
        
    def soigner(self):
        if self.alive == True:
            if self.energie + 15 > 50:
                self.energie = 50
            else :
                self.energie += 15
           
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
    
#on définit les noms des joueurs 1 et 2

a = input("comment s'appelle le perso de l'utilisateur 1 ?")    
b = input("comment s'appelle le perso de l'utilisateur 2 ?")
at = ''
de = ''
choixclass1 = input("Quel type pour le J1? at : attaque, de : defense") #demande a l'utilisateur 1 la classe qu'il veut choisir
if choixclass1 == 'at' : 
    player1 = Att(a)
if choixclass1 == 'de' : 
    player1 = Def(a)                            #et repond a sa demande
choixclass2 = input("Quel type pour le J2? at : attaque, de: defense")  #demande a l'utilisateur 2 la classe qu'il veut choisir
if choixclass2 == 'at' : 
    player2 = Att(b)
if choixclass2 == 'de' :                        #et repond a sa demande
    player2 = Def(b) 
c = randint(1,2)            #tire un nombre entre 1 et 2
tour_1 = ''
tour_2 = ''
if c == 1:                  #si c'est 1, le joueur 1 commence, si c'est 2, le joueur 2 commence
    tour_1 = player1
    tour_2 = player2
    print('le joueur1 ',tour_1.get_nom(),'commence')
else:
    tour_1 = player2 
    tour_2 = player1
    print('le joueur2',tour_1.get_nom(),' commence')

while player1.is_alive() and player2.is_alive() == True:            #on verifie que les 2 joueurs soient en vie pour continuer
    print()
    print('Le joueur1',player1.get_nom(),'a',player1.get_energie(),'dénergie et le joueur2',player2.get_nom(),'a',player2.get_energie(),'dénergie')
    print('Au tour de',tour_1.get_nom(),'!')        #annonce les noms, les énergies, et le celui qui joue
    decision = input('Que veux tu faire?'           #creation d'une variable decision qui demande a l'utilisateur ce qu'il veut faire
                     ' a : attaquer'
                     ' s : soigner'
                     ' as : attaque speciale'
                     ' ss : soin special') 
    if decision == 'a':                             #applique sa decision
        tour_2.blesser()
    if decision == 's':
        tour_1.soigner()
    if decision == 'as':
        tour_2.att_spe()
    if decision == 'ss':
        tour_1.soin_spe()
    
    print()
    if tour_2.is_alive() == True:           #on verifie la vie pour le tour 2 aussi et on fais pareil pour les annonces et decisions
        print('Le joueur1',player1.get_nom(),'a',player1.get_energie(),'dénergie et le joueur2',player2.get_nom(),'a',player2.get_energie(),'dénergie')
        print('Au tour de',tour_2.get_nom(),'!')
        decision = input('Que veux tu faire?'
                         ' a : attaquer'
                         ' s : soigner'
                         ' as : attaque speciale'
                         ' ss : soin special') 
        if decision == 'a':
            tour_1.blesser()
        if decision == 's':
            tour_2.soigner()
        if decision == 'as':
            tour_1.att_spe()
        if decision == 'ss':
            tour_2.soin_spe()
        
if player1.is_alive() == False:             #annonce qui gagne
    print(player2.get_nom(),'gagne !')
if player2.is_alive() == False:
    print(player1.get_nom(),'gagne !')




    
