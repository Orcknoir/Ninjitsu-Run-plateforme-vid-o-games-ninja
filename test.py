

#!/usr/bin/python
# coding: utf-8
 
import pygame
from pygame.locals import *
 
def main():
    # Initialisation de la fenêtre d'affichage
    pygame.init()
    screen = pygame.display.set_mode((300, 50))
    pygame.display.set_caption('Programme Pygame de base')
 
    # Remplissage de l'arrière-plan
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
 
    # Affichage d'un texte
    font = pygame.font.Font(None, 36)
    text = font.render("Salut tout le monde", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)
 
    # Afficher le tout dans la fenêtre
    screen.blit(background, (0, 0))
    pygame.display.flip()
 
    # Boucle d'évènements
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
 
        screen.blit(background, (0, 0))
        pygame.display.flip()
 
if __name__ == '__main__': main()

import sys
import random
import math
import os
import getopt
import pygame
from socket import *
from pygame.locals import *

try:
    pass  # Code qui peut générer des ImportError
except ImportError as err:
    print("Impossible de charger le module. %s" % (err))
    sys.exit(2)

def load_png(name):
    """Charge une image et retourne un objet image"""
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print("Impossible de charger l'image : ", fullname)
        raise SystemExit(message)
    return image, image.get_rect()
class Ball:
    def __init__(self):
        # Initialiser les attributs de la balle ici
        pass

    def update(self):
        # Mettre à jour la position de la balle ici
        pass

    def check_borders(self):
        # Vérifier si la balle touche les bords ici
        pass

# Fonction principale
def main():
    # Initialiser l'environnement du jeu ici

    # Créer un nouvel objet, instance de la classe Ball
    ball = Ball()

    while True:
        # Vérifier les entrées utilisateur

        # Appel de la méthode update() de la balle
        ball.update()

# Lancement du jeu
if __name__ == "__main__":
    main()
class Ball(pygame.sprite.Sprite):
        """Une balle qui se déplace sur lécran
        Retourne: objet ball
        Fonctions: update, calcNewPos
        Attributs: area, vector"""
 
        def __init__(self, vector):
                pygame.sprite.Sprite.__init__(self)
                self.image, self.rect = load_png('ball.png')
                screen = pygame.display.get_surface()
                self.area = screen.get_rect()
                self.vector = vector
 
        def update(self):
                newPos = self.calcNewPos(self.rect,self.vector)
                self.rect = newPos
 
        def calcNewPos(self,rect,vector):
                (angle,z) = vector
                (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
                return rect.move(dx,dy)
                
