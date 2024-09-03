import pygame
import sys
import json

# Inicializa o Pygame
pygame.init()

# Configurações de tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Editor de Níveis")

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 128, 255)

def save_level(filename, elements):
    level_data = [{"x": e.x, "y": e.y, "width": e.width, "height": e.height} for e in elements]
    with open(filename, 'w') as f:
        json.dump(level_data, f)

def load_level(filename):
    with open(filename, 'r') as f:
        level_data = json.load(f)
    elements = [pygame.Rect(data["x"], data["y"], data["width"], data["height"]) for data in level_data]
    return elements

# Função principal do editor
def main():
    running = True
    elements = []
    selected_element = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  # Pressione 's' para salvar
                    save_level("user_levels/level1.json", elements)
                elif event.key == pygame.K_l:  # Pressione 'l' para carregar
                    elements = load_level("user_levels/level1.json")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clique esquerdo
                    pos = pygame.mouse.get_pos()
                    for element in elements:
                        if element.collidepoint(pos):
                            selected_element = element
                            break
                    else:
                        rect = pygame.Rect(pos[0], pos[1], 50, 50)
                        elements.append(rect)
                elif event.button == 3:  # Clique direito
                    pos = pygame.mouse.get_pos()
                    for element in elements:
                        if element.collidepoint(pos):
                            elements.remove(element)
                            break
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    selected_element = None
            elif event.type == pygame.MOUSEMOTION:
                if selected_element:
                    selected_element.x = event.pos[0] - selected_element.width // 2
                    selected_element.y = event.pos[1] - selected_element.height // 2

        screen.fill(white)
        for element in elements:
            pygame.draw.rect(screen, blue, element)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
