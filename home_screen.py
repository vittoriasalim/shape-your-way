import pygame

# Constants
WHITE = (0xFF, 0xFF, 0xFF)
BLACK_COLOR=(0,0,0)
BG_COLOR = ((192,192,192))
RECT_COLOR = (105,105,105)
TEXT_COLOR = (211,211,211)
GREY_COLOR=(255,255,255)
SCREEN_WIDTH = 990
SCREEN_HEIGHT = 660
DUNGEON_BG = ("./images/dungeon_bg.jpeg")
CAVE_BG =("./images/purple_dg_bg.png")

class HomeScreen():
    """
    Home Screen (or Main Screen)
    """
    def __init__(self, screen):

        self.screen = screen
        self.is_running = False
        self.endFont = pygame.font.SysFont("Helvetica", 70, bold=True)
        self.buttonFont = pygame.font.SysFont("Rammetto One", 40, bold=True)

    def draw(self):
        bg = pygame.image.load(CAVE_BG)
        self.screen.blit(bg,(0,0))
        # Create header "Roll Your Way" on home screen
        #pygame.draw.rect(self.screen, RECT_COLOR, pygame.Rect(195, 60, 600, 100))
        label = self.endFont.render("SHAPE YOUR WAY", 1, GREY_COLOR)
        self.screen.blit(label, (240, 170))

        # Create "Start" button
        #pygame.draw.rect(self.screen, (164, 182, 229, 1), pygame.Rect(305, 350, 400, 400), 10)
        #pygame.draw.rect(self.screen, (164, 182, 229, 1), pygame.Rect(423, 440, 150, 50))
        #pygame.draw.rect(self.screen, BG_COLOR, pygame.Rect(423, 440, 150, 50), 5)
        mouse = pygame.mouse.get_pos()
        if 450 <= mouse[0] <= 600 and 350 <= mouse[1] <= 400:
            label_button = self.buttonFont.render("START", 1, BG_COLOR)
        else:
            label_button = self.buttonFont.render("START", 1, WHITE)
        self.screen.blit(label_button, (450, 350))
        if 460 <= mouse[0] <= 600 and 420 <= mouse[1] <= 470:
            label_button2 = self.buttonFont.render("EXIT", 1, BG_COLOR)
        else:
            label_button2 = self.buttonFont.render("EXIT", 1, WHITE)
        self.screen.blit(label_button2, (460, 420))

    def mainloop(self) -> bool:

        self.is_running = True
        while (self.is_running):

            # frame per second
            pygame.time.delay(50)

            # events
            mouse = pygame.mouse.get_pos()
            for ev in pygame.event.get():

                if ev.type == pygame.QUIT:
                    pygame.quit()
                    return True

                # checks if a mouse is clicked
                if ev.type == pygame.MOUSEBUTTONDOWN:

                    # if the mouse is clicked on the
                    # button, go to the game page
                    if 450 <= mouse[0] <= 600 and 350 <= mouse[1] <= 400:
                        self.is_running = False
                    
                    if 460 <= mouse[0] <= 600 and 420 <= mouse[1] <= 470:
                        pygame.quit()
                        return True

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
    surface = pygame.display.set_mode((990,660))
    pygame.display.set_caption("Shape Your Way")

    # main loop in homescreen
    HomeScreen(surface).mainloop()