import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des variables
largeur_fenetre = 800
hauteur_fenetre = 600
position_x = 400
position_y = 300
largeur_personnage = 50
hauteur_personnage = 50
vitesse = 5
saut = False
hauteur_saut = 10
gravite = 1
immobile = True

# Configuration de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Personnage en mouvement")

# Chargement des sprites du personnage
sprites_droite = [pygame.image.load(f"personnage_droite{i}.png") for i in range(1, 4)]
sprites_gauche = [pygame.image.load(f"personnage_gauche{i}.png") for i in range(1, 4)]
sprite_saut = pygame.image.load("personnage_saut.png")
sprite_immobile = pygame.image.load("personnage_immobile.png")

personnage_rect = sprites_droite[0].get_rect()
sprite_index = 0

# Plateformes
plateformes = [pygame.Rect(0, 500, 200, 20), pygame.Rect(400, 400, 200, 20), pygame.Rect(700, 300, 200, 20)]

# Boucle principale
continuer = True
while continuer:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            continuer = False

    # Déplacement du personnage
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT]:
        position_x -= vitesse
        sprite_list = sprites_gauche
        immobile = False
    elif touches[pygame.K_RIGHT]:
        position_x += vitesse
        sprite_list = sprites_droite
        immobile = False
    else:
        immobile = True

    # Animation du personnage
    if saut:
        personnage_image = sprite_saut
    elif not immobile:
        sprite_index = (sprite_index + 1) % len(sprite_list)
        personnage_image = sprite_list[sprite_index]
    else:
        personnage_image = sprite_immobile

    # Gestion du saut
    if saut:
        position_y -= hauteur_saut
        hauteur_saut -= gravite
        if position_y >= 300:  # Ajustez cette valeur selon la hauteur du sol
            position_y = 300
            saut = False
            hauteur_saut = 10

    # Gestion de la gravité
    if position_y < 300:  # Ajustez cette valeur selon la hauteur du sol
        position_y += gravite
    else:
        position_y = 300  # Ajustez cette valeur selon la hauteur du sol

    # Détecter la touche pour sauter
    if touches[pygame.K_SPACE] and not saut and position_y == 300:  # Vérifie si le personnage est sur une plateforme pour sauter
        saut = True

    # Vérification des collisions avec les plateformes
    for plateforme in plateformes:
        if personnage_rect.colliderect(plateforme) and hauteur_saut < 0:
            hauteur_saut = 0
            position_y = plateforme.top - hauteur_personnage

    # Rafraîchissement de l'écran
    fenetre.fill((255, 255, 255))  # Fond blanc
    fenetre.blit(personnage_image, (position_x, position_y))  # Affichage du sprite du personnage

    # Dessiner les plateformes
    for plateforme in plateformes:
        pygame.draw.rect(fenetre, (0, 0, 255), plateforme)

    pygame.display.flip()

    # Limite de la vitesse de rafraîchissement
    pygame.time.Clock().tick(30)

# Quitter Pygame
pygame.quit()
sys.exit()
