import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu avec Personnage")

# Propriétés du personnage
player_size = 50
player_color = WHITE
player_rect = pygame.Rect(WIDTH // 2 - player_size // 2, HEIGHT // 2 - player_size // 2, player_size, player_size)
player_speed = 5
jump_height = 15
gravity = 1.5  # Ajustez la gravité selon vos besoins
is_jumping = False
jump_count = 15  # Ajustez le nombre de frames pour contrôler la hauteur du saut

# Propriétés du sol
ground_height = HEIGHT - 20

# Boucle de jeu
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mouvement du personnage avec les touches fléchées
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.move_ip(-player_speed, 0)
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.move_ip(player_speed, 0)

    # Saut du personnage
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
    else:
        if jump_count >= -15:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_rect.move_ip(0, -((jump_count ** 2) * 0.5) * neg)
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 15

    if player_rect.bottom < ground_height:
        player_rect.move_ip(0, gravity)
        gravity += 0.5  # Ajustez la gravité selon vos besoins
    else:
        gravity = 1.5

    # Dessiner l'arrière-plan
    screen.fill(BLACK)

    # Dessiner le sol
    pygame.draw.rect(screen, RED, (0, ground_height, WIDTH, HEIGHT - ground_height))

    # Dessiner le personnage (carré)
    pygame.draw.rect(screen, player_color, player_rect)

    pygame.display.flip()
    clock.tick(60)
