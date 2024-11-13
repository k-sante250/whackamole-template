import pygame
import random

square_size = 32
black = (0, 0, 0)

def draw_map(screen):
    for i in range(square_size, 640, square_size):
        pygame.draw.line(screen, black, (i, 0), (i, 512))
    for i in range(square_size, 512, square_size):
        pygame.draw.line(screen, black, (0, i), (640, i))

def grid_position(a):
    return a // square_size

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        mole_x, mole_y = 0, 0
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    x = grid_position(x)
                    y = grid_position(y)
                    if x == mole_x and y == mole_y:
                        mole_x, mole_y = grid_position(random.randrange(0, 640)), grid_position(random.randrange(0, 512))
                        while x == mole_x and y == mole_y:
                            mole_x, mole_y = grid_position(random.randrange(0, 640)), grid_position(random.randrange(0, 512))
            screen.fill("light green")
            draw_map(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x * square_size, mole_y * square_size)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
