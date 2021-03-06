import pygame
from pygame.locals import *
import graphe_oriente
import joueur
import random

# lancement des modules inclus dans pygame
pygame.init() 
# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("comicsansms", 30)
# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800,600), NOFRAME)
pygame.display.set_caption("Jeu de Nim") 
# chargement de l'image de fond
fond = pygame.image.load('background.png')

# creation des joueurs
player1 = joueur.Joueur()
player2 = joueur.Joueur()

# creation du graphe de jeu pour l'intelligence artificielle
G = graphe_oriente.GraphOriente()
###à compléter Partie B : question 2)
for i in range(1,13):
    G.ajouter_sommet(i)
    if i>3 :
        G.ajouter_arc(i,i-1)
        G.ajouter_arc(i,i-2)
        G.ajouter_arc(i,i-3)
G.ajouter_arc(3,2)
G.ajouter_arc(3,1)
G.ajouter_arc(2,1)




#ajouter les arcs

##créer le graphe de tous les coups possibles sommets + arcs
'''
screen.blit(zone1,(120,550))
screen.blit(zone2,(170,550))
screen.blit(zone3,(220,550))
screen.blit(zone1,(510,550))
screen.blit(zone2,(560,550))
screen.blit(zone3,(610,550))
'''       
#boutons cliquables joueur 1
zone1 = pygame.image.load("b1.png") #image du bouton
zone1rect = pygame.Rect(120,550,30,30) #rectangle autour de l'image (10,10) coordonnées et (30,30) largeur et hauteur
zone2 = pygame.image.load("b2.png")
zone2rect=pygame.Rect(170,550,30,30)
zone3 = pygame.image.load("b3.png")
zone3rect = pygame.Rect(220,550,30,30)

#boutons cliquables joueur2
zone4rect = pygame.Rect(510,550,30,30)
zone5rect = pygame.Rect(560,550,30,30)
zone6rect = pygame.Rect(610,550,30,30)

#reponse question rejouer :
oui = pygame.image.load("oui.png")
ouirect = pygame.Rect(10,450,50,50)

non = pygame.image.load("non.png")
nonrect = pygame.Rect(70,450,50,50)


#allumettes
nbAllumettes = 12
allumette = pygame.image.load('invader1.png')

running = True # variable de la boucle de jeu
#choix du joueur qui commence au hasard
n = random.randint(1,2)
if n == 1 :
    player1.joue = True
else :
    player2.joue = True
    
#variables de gestion de fin de partie
fin = False
augmente_score = False

###Boucle MENU : au choix : 2 joueurs humains ou 1 humain contre ordi en IA apprenante
menu = True

fondmenu = pygame.image.load("menu.png")
button_vs_ia = pygame.image.load("button_vs-computer.png")
button_vs_player = pygame.image.load("button_vs-player.png")
button_rules = pygame.image.load("button_the-rules.png")
button_close = pygame.image.load("button_close.png")
#
buttonia_rect = button_vs_ia.get_rect()
buttonia_rect.x, buttonia_rect.y = 270, 350
#
buttonplayer_rect = button_vs_player.get_rect()
buttonplayer_rect.x, buttonplayer_rect.y = 270, 250
#
buttonrules_rect = button_rules.get_rect()
buttonrules_rect.x, buttonrules_rect.y = 270, 150
#
buttonclose_rect = button_close.get_rect()
buttonclose_rect.x, buttonclose_rect.y = 740,10
#
humainVShumain = False
humainVSordi = False

vitesse=50

while menu :
    screen.blit(fondmenu,(0,0))
    screen.blit(button_rules,(270, 150))
    screen.blit(button_vs_player,(270, 250))
    screen.blit(button_vs_ia,(270, 350))
    screen.blit(button_close,(740,10))
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            menu = False # menu est sur False
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
                #verification pour savoir si la souris est sur le bouton jouer
                if buttonplayer_rect.collidepoint(event.pos):
                    humainVShumain = True
                    menu = False
                    player1.set_etat("humain")
                    player2.set_etat("humain")
                    print("Lancement jeu vs joueur")
                if buttonia_rect.collidepoint(event.pos):
                    humainVSordi = True
                    menu = False
                    player1.set_etat("humain")
                    player2.set_etat("ordi")
                    print("Lancement jeu vs computer")
                if buttonrules_rect.collidepoint(event.pos):
                    print("Menu des Règles")
                if buttonclose_rect.collidepoint(event.pos):
                    menu = False # menu est sur False
                    running = False

                        
    pygame.display.update()
### BOUCLE DE JEU  ###
while running : # boucle infinie pour laisser la fenêtre ouverte
    if humainVShumain : 
        # dessin du fond
        screen.blit(fond,(0,0))
        screen.blit(button_close,(740,10))
        if player1.joue == True:
            labelJ = myfont.render("joueur1 joue", 1, (255,255,255))
            screen.blit(labelJ, (320, 10))
        if player2.joue == True:
            labelJ2 = myfont.render("joueur2 joue", 1, (255,255,255))
            screen.blit(labelJ2, (320, 10))
        #affichage des allumettes :
        for i in range( nbAllumettes) :
            screen.blit(allumette,(vitesse,i*35+100))

        ### Gestion des événements  ###
        for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
            if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                running = False # running est sur False
                
           
           # gestion de la souris
            elif event.type == MOUSEBUTTONUP: # quand je relache le bouton
                if event.button == 1: # 1= clique gauche
                    if zone1rect.collidepoint(event.pos) and player1.joue == True:
                        print(1)
                        if nbAllumettes>=2 :
                            vitesse+=100
                            nbAllumettes -=1
                            player1.joue = False
                            player2.joue = True
                    if zone2rect.collidepoint(event.pos) and player1.joue == True:
                        print(2)
                        if nbAllumettes>=3 :
                            vitesse+=100
                            nbAllumettes -=2
                            player1.joue = False
                            player2.joue = True
                    if zone3rect.collidepoint(event.pos) and player1.joue == True:
                        print(3)
                        if nbAllumettes>=4 :
                            vitesse+=100
                            nbAllumettes -=3
                            player1.joue = False
                            player2.joue = True
                    if zone4rect.collidepoint(event.pos) and player2.joue == True:
                        print(1)
                        if nbAllumettes>=2 :
                            vitesse+=100
                            nbAllumettes -=1
                            player1.joue = True
                            player2.joue = False
                    if zone5rect.collidepoint(event.pos) and player2.joue == True:
                        print(2)
                        if nbAllumettes>=3 :
                            nbAllumettes -=2
                            vitesse+=100
                            player1.joue = True
                            player2.joue = False
                    if zone6rect.collidepoint(event.pos) and player2.joue == True:
                        print(3)
                        if nbAllumettes>=4 :
                            nbAllumettes -=3
                            vitesse+=100
                            player1.joue = True
                            player2.joue = False
                    ###Question 2) compléter pour les 5 autres zones correspondant aux boutons de jeux
                    ###Pour rejouer, on teste si le joueur appuie sur oui ou non    
                    if ouirect.collidepoint(event.pos) :
                        fin = False
                        #on choisit au hasard qui joue
                        n = random.randint(1,2)
                        if n == 1 :
                            player1.joue = True
                        else :
                            player2.joue = True
                        nbAllumettes = 12
                        player1.gagne = False
                        player2.gagne = False
                    if nonrect.collidepoint(event.pos) :
                        running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttonclose_rect.collidepoint(event.pos):
                    menu = False # menu est sur False
                    running = False


        screen.blit(zone1,(120,550))
        screen.blit(zone2,(170,550))
        screen.blit(zone3,(220,550))
        screen.blit(zone1,(510,550))
        screen.blit(zone2,(560,550))
        screen.blit(zone3,(610,550))

        if nbAllumettes == 1 and player1.joue == True :
            print('joueur2 gagne')
            fin = True
            player2.gagne = True
            vitesse = 50
            # render text
            player2.joue = None
            player1.joue = None
            augmente_score = True
        if nbAllumettes == 1 and player2.joue == True :
            print('joueur1 gagne')
            fin = True
            player1.gagne = True
            vitesse = 50
            # render text
            player2.joue = None
            player1.joue = None
            augmente_score = True
        if fin == True :
            if player1.gagne :
                label = myfont.render("Le gagnant est joueur1", 1, (255,255,255))
                if augmente_score == True :
                    player1.score+=1
                    augmente_score = False
                    
            else :
                label = myfont.render("Le gagnant est joueur2", 1, (255,255,255))
                if augmente_score == True :
                        player2.score+=1
                        augmente_score = False
                   
            question = myfont.render("Une nouvelle partie ?",1,(255,255,255))
            score = myfont.render("joueur 1 a "+str(player1.score)+" points et le joueur 2 a "+str(player2.score)+"points",1,(255,255,255))
            screen.blit(label, (200, 10))
            screen.blit(question,(10,400))
            screen.blit(oui,(10,450))
            screen.blit(non,(70,450))
            screen.blit(score,(10,500))
    if humainVSordi :
            # dessin du fond
            screen.blit(fond,(0,0))
            screen.blit(button_close,(740,10))
            if player1.joue == True:
                labelJ = myfont.render("joueur1 joue", 1, (0,0,255))
                screen.blit(labelJ, (320, 10))
            if player2.joue == True:
                labelJ2 = myfont.render("joueur2 joue", 1, (0,0,255))
                screen.blit(labelJ2, (320, 10))
            #affichage des allumettes :
            for i in range(nbAllumettes) :
                screen.blit(allumette,(vitesse,i*35+100))

            ### Gestion des événements  ###
            for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
                if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                    running = False # running est sur False
                    
               
               # gestion de la souris
                elif event.type == MOUSEBUTTONUP: # quand je relache le bouton
                    if event.button == 1: # 1= clique gauche
                        if zone1rect.collidepoint(event.pos) and player1.joue == True:
                            print(1)
                            if nbAllumettes>=2 :nbAllumettes -=1
                            player1.joue = False
                            player2.joue = True
                            vitesse+=200
                        if zone2rect.collidepoint(event.pos) and player1.joue == True :
                            print(2)
                            if nbAllumettes>=3 :nbAllumettes -=2
                            player1.joue = False
                            player2.joue = True
                            vitesse+=200
                        if zone3rect.collidepoint(event.pos) and player1.joue == True :
                            print(3)
                            if nbAllumettes>=4 :nbAllumettes -=3
                            player1.joue = False
                            player2.joue = True
                            vitesse+=200
                        #il n'y a plus que les trois boutons du joueur humain
                        if ouirect.collidepoint(event.pos) :
                            fin = False
                            n = random.randint(1,2)
                            if n == 1 :
                                player1.joue = True
                            else :
                                player2.joue = True
                            nbAllumettes = 12
                            player1.gagne = False
                            player2.gagne = False
                        if nonrect.collidepoint(event.pos) :
                            running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if buttonclose_rect.collidepoint(event.pos):
                        menu = True # menu est sur False
                        running = False
            #on affiche que les trois boutons de l'humain
            screen.blit(zone1,(120,550))
            screen.blit(zone2,(170,550))
            screen.blit(zone3,(220,550))
            #l'ordi choisi son coup :
            if player2.joue == True and nbAllumettes >1 :
                #à compléter Partie B question 3) le player2 ordi doit choisir son coups grâce au graphe G des coups
                #il doit choisir au hasard parmi la liste des arcs issus du sommet correspondant au nb d'allumettes
                liste_voisins = G.liste_sommets_issus(nbAllumettes)
                nbAllumettes = random.choice(liste_voisins)
                player2.joue=False
                player1.joue = True
                # à compléter partie C question 2) : gérer si la liste de coups issus du nbd'allumettes présente est vide (gobelet vide dans vidéo)

            if nbAllumettes == 1 and player1.joue == True :
                print('joueur2 gagne')
                fin = True
                vitesse=50
                player2.gagne = True
                player2.joue = None
                player1.joue = None
                augmente_score = True
            if nbAllumettes == 1 and player2.joue == True :
                print('joueur1 gagne')
                fin = True
                vitesse=50
                player1.gagne = True
                player2.joue = None
                player1.joue = None
                augmente_score = True
                #Partie C : question 1) Si le joueur humain gagne , l'ordi supprime son dernier coups pour ne plus le refaire
                
            if fin == True :
                if player1.gagne :
                    label = myfont.render("Le gagnant est joueur1", 1, (255,255,255))
                    if augmente_score == True :
                        player1.score+=1
                        augmente_score = False
                        
                else :
                    label = myfont.render("Le gagnant est joueur2", 1, (255,255,255))
                    if augmente_score == True :
                        player2.score+=1
                        augmente_score = False
                        
                question = myfont.render("Voulez-vous rejouer ?",1,(255,255,255))
                score = myfont.render("joueur 1 a "+str(player1.score)+" points et le joueur 2 a "+str(player2.score)+"points",1,(255,255,255))
                screen.blit(label, (200, 10))
                screen.blit(question,(10,400))
                screen.blit(oui,(10,450))
                screen.blit(non,(70,450))
                screen.blit(score,(10,500))
    pygame.display.update() # pour ajouter tout changement à l'écran
pygame.quit()