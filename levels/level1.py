import pygame

def load_level():
    player = pygame.Rect(50, 50, 50, 50)  # Posição inicial do jogador
    return [player]

def update_level(screen, elements):
    player = elements[0]
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    pygame.draw.rect(screen, (0, 128, 255), player)
