import pygame
import parse
from game import Game

# Constants
WHITE = (0xFF, 0xFF, 0xFF)

BG_COLOR = (62, 61, 100)
RECT_COLOR = (233, 226, 246)

SCREEN_WIDTH = 990
SCREEN_HEIGHT = 660


class LorePage():
    """
    Winning Screen (or End Screen)
    """

    def __init__(self, screen, data):

        self.screen = screen
        self.data = data
        self.is_running = False
        self.endFont = pygame.font.SysFont("Rammetto One", 80, bold=True)
        self.textFont = pygame.font.SysFont("Rammetto One", 20, bold=False)
        self.buttonFont = pygame.font.SysFont("Rammetto One", 40, bold=True)

    def draw(self):
        #pygame.draw.rect(self.screen, RECT_COLOR, pygame.Rect(195, 60, 600, 550))
        congrats_message = self.endFont.render("Congratulations!", 1, WHITE)
        self.screen.blit(congrats_message, (230, 210))
        way_message = self.buttonFont.render("You have just made your way through the dungeon!", 1, WHITE)
        enter_to_quit = self.textFont.render("Please press ENTER to quit!",True,WHITE)
        self.screen.blit(way_message,(100,300))
        self.screen.blit(enter_to_quit, (400, 380))
        # Create "Start" button

        mouse = pygame.mouse.get_pos()


    def mainloop(self):

        self.is_running = True
        while (self.is_running):

            # frame per second
            pygame.time.delay(50)

            # events
            mouse = pygame.mouse.get_pos()
            for ev in pygame.event.get():

                if ev.type == pygame.QUIT:
                    pygame.quit()

                # checks if a mouse is clicked
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_RETURN:
                    # if the mouse is clicked on the
                    # button, go to the game page
                        pygame.quit()

            # draw
            self.screen.fill(BG_COLOR)
            self.draw()
            pygame.display.update()
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

    # load the levels and data
    levels = parse.parse_json()
    data = parse.read_map(levels[0]['path'])

    print("Successfully parsing data for level 1")

    # main loop in homescreen
    WinningScreen(surface,data).mainloop()

    # quit the game properly
    pygame.quit()