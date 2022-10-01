import pygame
import parse
import time
# Constants
WHITE = (0xFF, 0xFF, 0xFF)

BG_COLOR = (62, 61, 100)
RECT_COLOR = (233, 226, 246)
TEXT_COLOR = (211,211,211)
SCREEN_WIDTH = 990
SCREEN_HEIGHT = 660


class LorePage():
    """
    Winning Screen (or End Screen)
    """

    def __init__(self, screen):

        self.screen = screen
        self.is_running = False
        self.endFont = pygame.font.SysFont("Rammetto One", 80, bold=True)
        self.textFont = pygame.font.SysFont("Rammetto One", 30, bold=False)
        self.buttonFont = pygame.font.SysFont("Rammetto One", 20, bold=True)

    def draw(self):
        bg = pygame.image.load("./images/dragon_bg.jpg")
        self.screen.blit(bg,(0,0))

        first_message = self.textFont.render("You have been kidnapped by an evil wizard for his experiment", 1, TEXT_COLOR)
        second_message = self.textFont.render("        You have been turned into a cube due to his magic ", 1, TEXT_COLOR)
        third_message = self.textFont.render("          You have been put into captivity into a dungeon",1,TEXT_COLOR)
        fourth_message = self.textFont.render("Your only hope to survive is to make your way through his dungeon ", 1, TEXT_COLOR)
        fifth_message = self.textFont.render("  You vow to return to your loved ones and turn back into human ",True,TEXT_COLOR)

        enter_to_proceed = self.buttonFont.render("Press ENTER to shape your way",True,TEXT_COLOR)
        self.screen.blit(first_message,(200,150))
        self.screen.blit(second_message, (200, 200))
        self.screen.blit(third_message, (200, 250))
        self.screen.blit(fourth_message,(200,300))
        self.screen.blit(fifth_message,(200,350))
        if time.time() %1 >0.5:
            self.screen.blit(enter_to_proceed,(730,600))
        # Create "Start" button

        mouse = pygame.mouse.get_pos()


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
                    # if the mouse is clicked on the
                    # button, go to the game page
                        self.is_running = False

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
    LorePage(surface,data).mainloop()

    # quit the game properly
    pygame.quit()