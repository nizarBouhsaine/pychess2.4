import pygame, sys
from button import Button
from main import main

WIDTH = 720
HEIGHT = 720

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
# le nom de la fenetre
pygame.display.set_caption("Chess game")

BG = pygame.transform.smoothscale(pygame.image.load("assets/background.jpg"), (WIDTH, HEIGHT))
black = (0, 0, 0)


def get_font(size):  # responsable d'afficher l'écriture sous la taille choisie (size)
    return pygame.font.Font(None, size)


def main_menu():
    pygame.init()
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Chess Game", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH // 2, 100))

        PvP_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(WIDTH // 2, 250),
                            text_input="Mode Player", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        PvAI_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(WIDTH // 2, 400),
                             text_input="Mode Computer", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(WIDTH // 2, 550),
                             text_input="QUIT", font=get_font(60), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # respensable du changement de la couleur quand la souris est sur l'élément
        for button in [PvP_BUTTON, PvAI_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if PvP_BUTTON.checkForInput(MENU_MOUSE_POS):
                        main()
                        # pygame.quit()
                        # sys.exit()
                    if PvAI_BUTTON.checkForInput(MENU_MOUSE_POS):
                        main(False)

                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    main_menu()
