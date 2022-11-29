
from random import randint
from tkinter import *


class Att :
    def __init__ (self,nom):

        self.nom = nom
        self.energie = 50                                  #sa met l'energie à 50 de base et on verifie si les joueurs sont en vie
        self.alive = True

    def soigner(self):
        if self.alive == True:
            if self.energie + 10 > 50:                   #pour la classe attaque , donc si l'energie est supérieure à 50 on l'a remet à 50
                self.energie = 50                         # on se soigne de 10 pour la classe attaque
            else :
                self.energie += 10

    def blesser(self):
        self.energie -= 15                               #l'attaque inflige donc 15 d'energie
        if self.energie <= 0:
            self.alive = False

    def att_spe(self):
        att_special = randint(0,20)                     #attaque spéciale , sa tire un nombre aléatoire entre 0 et 20 et sa inflige le nombre d'énergie tiré par ex si 3 tiré sa inflige 3 d'énergie
        self.energie -= att_special
        if self.energie <= 0:
            self.alive = False

    def soin_spe(self):
        if self.alive == True:
            soin_special = randint(0,20)
            if self.energie + soin_special > 50 :       # soin spécial c'est la même chose que pour l'attaque spé sauf que c'est le soin
                self.energie = 50
            else :
                self.energie += soin_special

    def get_nom(self):
        return self.nom

    def get_energie(self):
        return self.energie                             #je vais pas expliquer ses lignes c'est ce qu'on fait depuis le début

    def is_alive(self):
        return self.alive

    def __str__(self):
        return f"{self.nom},{self.energie}"


class Def :
    def __init__ (self,nom):

        self.nom = nom
        self.energie = 60                               #la classe def a plus de vie que l'attaque , elle commence à 60 d'énergie
        self.alive = True

    def soigner(self):
        if self.alive == True:
            if self.energie + 15 > 50:                  # le soin de base soigne de 15 vu que c'est la classe défense
                self.energie = 50
            else :
                self.energie += 15

    def blesser(self):
        self.energie -= 8                               #l'attaque de base inflige 8 d'énergie vu qu'il s'agit de la classe défense
        if self.energie <= 0:
            self.alive = False

    def att_spe(self):
        att_special = randint(0,15)
        self.energie -= att_special                     #pareil que la classe attaque sa tire un nombre aléatoire , ici entre 0 et 15 vu que c'est classe défense on inflige moin d'énergie
        if self.energie <= 0:
            self.alive = False

    def soin_spe(self):
        if self.alive == True:
            soin_special = randint(0,30)                #soin spécial , on tire entre 0 et 30 c'est plus que la classe attaque car c'est la classe défense donc plus de soin moins d'attaque
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
b = input("comment s'appelle le perso de l'utilisateur 2 ?")            #on demande aux joueurs comment ils s'appellent
at = ''
de = ''
choixclass1 = input("Quel type pour le J1? at : attaque, de : defense") #on demande pour lee joueur 1 quel classe choisie t'il entre attaque et defense
if choixclass1 == 'at' :
    player1 = Att(a)
if choixclass1 == 'de' :
    player1 = Def(a)
choixclass2 = input("Quel type pour le J2? at : attaque, de: defense") #pareil pour le joueur 2
if choixclass2 == 'at' :
    player2 = Att(b)
if choixclass2 == 'de' :
    player2 = Def(b)
c = randint(1,2)                                                        #on tire aléatoirement qui va commencer entre le joueur 1 et 2
tour_1 = ''
tour_2 = ''
if c == 1:
    tour_1 = player1                                                   #si 1 c'est le joueur 1 qui commence , si 2 c'est le joueur 2 qui commence
    tour_2 = player2
    print('le joueur1 ',tour_1.get_nom(),'commence')
else:
    tour_1 = player2
    tour_2 = player1
    print('le joueur2',tour_1.get_nom(),' commence')

while player1.is_alive() and player2.is_alive() == True:
    print()
    print('Le joueur1',player1.get_nom(),'a',player1.get_energie(),'dénergie et le joueur2',player2.get_nom(),'a',player2.get_energie(),'dénergie')  #sa affiche les attributs de joueur et apres sa dit c'est au tour de quel joueur
    print('Au tour de',tour_1.get_nom(),'!')
    root = Tk()
    bouton1 = Button(root, text='Attaque', width=20, command=tour_2.blesser())
    bouton1.pack(pady=10)
    bouton2 = Button(root, text='Defense', width=20, command=tour_1.soigner())
    bouton2.pack(pady=10)                                                                         #les quatre lignes servent à ouvrir un fenetre tk inter avec des boutons associés à chaque commande d'attaque et de soin
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
        bouton6.pack(pady=10)                                                                       #pareil mais pour le joueur 2
        bouton7 = Button(root, text='Attaque spéciale', width=20, command=tour_1.att_spe())
        bouton7.pack(pady=10)
        bouton8 = Button(root, text='Défense spéciale', width=20, command=tour_2.soin_spe())
        bouton8.pack(pady=10)
        root.mainloop()


if player1.is_alive() == False:
    print(player2.get_nom(),'gagne !')
if player2.is_alive() == False:                             #si le joueur 1 est mort c'est à dire qu'il n'a plus d'énergie le joueur 2 gagne
    print(player1.get_nom(),'gagne !')                      #si le joueur 2 est mort c'est à dire qu'il n'a plus d'énergie le joueur 1 gagne