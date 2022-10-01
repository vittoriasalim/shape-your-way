import pygame

# Constants
WHITE = (0xFF, 0xFF, 0xFF)

BG_COLOR = (62, 61, 100)
RECT_COLOR = (233, 226, 246)

SCREEN_WIDTH = 990
SCREEN_HEIGHT = 660

class WinningScreen():
    """
    Winning Screen (or End Screen)

    The winning screen has these attributes:
    - screen: window
    - is_running: for the mainloop

    Fonts
    - endFont
    - textFont
    - buttonFont
    """
    def __init__(self, screen):

        # initialize pygame
        pygame.init()

        self.screen = screen
        self.is_running = False

        self.endFont = pygame.font.SysFont("Rammetto One", 80, bold=True)
        self.textFont = pygame.font.SysFont("Rammetto One", 20, bold=False)
        self.buttonFont = pygame.font.SysFont("Rammetto One", 40, bold=True)

    def draw(self):

        # Congratulations message (Label)
        congrats_message = self.endFont.render("Congratulations!", 1, WHITE)
        self.screen.blit(congrats_message, (230, 210))

        # Way message (Label)
        way_message = self.buttonFont.render("You have just made your way through the dungeon!", 1, WHITE)
        enter_to_quit = self.textFont.render("Please press ENTER to quit!",True,WHITE)
        self.screen.blit(way_message,(100,300))
        self.screen.blit(enter_to_quit, (400, 380))

    def mainloop(self):

        self.is_running = True
        while (self.is_running):

            # frame per second
            pygame.time.delay(50)

            # events
            for ev in pygame.event.get():

                if ev.type == pygame.QUIT:
                    pygame.quit()
                    return True

                # checks if a mouse is clicked
                if ev.type == pygame.KEYDOWN:

                    if ev.key == pygame.K_RETURN:
                        self.is_running = False

            # update the user interface
            self.screen.fill(BG_COLOR)
            self.draw()
            pygame.display.update()
        
        # quit the game
        pygame.quit()


# For testing
if (__name__ == "__main__"):
    print("--------------------")
    print("Console for the game")
    print("--------------------")

    # initialise the pygame
    pygame.init()
    press = False

    print("Creating a new window")

    # create the window
    surface = pygame.display.set_mode((990, 560))
    pygame.display.set_caption("Find Your Way Out")

    # main loop in homescreen
    WinningScreen(surface).mainloop()

    # quit the game properly
    pygame.quit()