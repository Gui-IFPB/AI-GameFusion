import pygame
import sys
from levels import level1

# Inicializa o Pygame
pygame.init()

# Configurações de tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo Educacional de Python")

# Cores
white = (255, 255, 255)

# Função principal do jogo
def main():
    running = True
    elements = level1.load_level()  # Carrega os elementos do nível

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(white)
        level1.update_level(screen, elements)  # Atualiza o nível
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
