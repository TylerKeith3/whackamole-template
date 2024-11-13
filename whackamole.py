import pygame
import random



def main():

    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_row = 0
        mole_col = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    print(mole_row,mole_col)
                    if (event.pos[0]//32, event.pos[1]//32) == (mole_row, mole_col):
                        # print(event.pos)
                        mole_row = random.randrange(0, 20)
                        mole_col = random.randrange(0, 15)
                        # x = x // 32
                        # y = y // 32
                        # x *= 32
                        # y *= 32
                        # mole_row = x
                        # mole_col = y
                        # screen.blit(mole_image, mole_image.get_rect(topleft=(mole_row, mole_col)))
                if event.type == pygame.QUIT:
                    running = False

            screen.fill("light green")

            for i in range(1, 21):
                pygame.draw.line(screen, 'black', (i * 32, 0), (i * 32, 512), 1)
            for i in range(1, 17):
                pygame.draw.line(screen, 'black', (0, i * 32), (640, i * 32), 1)

            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_row*32, mole_col*32)))
            pygame.display.flip()
            clock.tick(60)


    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
