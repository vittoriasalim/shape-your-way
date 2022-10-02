import pygame
from home_screen import HomeScreen
from game import Game
from tutorial import TutorialPage
from winning_screen import WinningScreen
from lore_page import LorePage

# Constants
WHITE = (0xFF, 0xFF, 0xFF)

BG_COLOR = (62, 61, 100)
RECT_COLOR = (233, 226, 246)

SCREEN_WIDTH = 990
SCREEN_HEIGHT = 660

# background music
MAIN_MENU_MUSIC = ("./sounds/Free Game Soundtrack by cactusdude - (hurry up).ogg")
MAIN_MENU_MUSIC2 = ("./sounds/sounds_8Bit Platformer Loop.ogg")
GAME_MUSIC= ("./sounds/Dystopian.ogg")
GAME_MUSIC2 = ("./sounds/Quantum Loop.ogg")
WINNING_SCREEN_MUSIC = ("./sounds/8Bit Jingle Bells Loop.ogg")

# icon for the game
WIZARD_ICON = pygame.image.load("./images/wizard_solo.png")

# Main App
class App():

    def __init__(self) -> None:

        print("--------------------")
        print("Console for the game")
        print("--------------------")

        # initialise the pygame
        pygame.init() # for the UI
        pygame.mixer.init() # for the audio

        print("Creating a new window")

        # create the window
        surface = pygame.display.set_mode((990,660))
        pygame.display.set_caption("Shape Your Way")
        pygame.display.set_icon(WIZARD_ICON)

        is_quit = False

        # Get the homescreen
        if (not is_quit):
            pygame.mixer.music.load(MAIN_MENU_MUSIC)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.5) # reduce the volume by 50%
            is_quit = HomeScreen(surface).mainloop()

        # lore, tutorial and game page: same music

        # go to the lore page
        if (not is_quit):
            pygame.mixer.music.load(GAME_MUSIC2)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.5) # reduce the volume by 50%
            is_quit = LorePage(surface).mainloop()

        # go to the tutorial page
        if (not is_quit):
            is_quit = TutorialPage(surface).mainloop()

        # start from level 1
        if (not is_quit):
            is_quit = Game(surface, 1).mainloop()

        # once the player passed all the game levels
        if (not is_quit):
            pygame.mixer.music.load(WINNING_SCREEN_MUSIC)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.5) # reduce the volume by 50%
            is_quit = WinningScreen(surface).mainloop()

        # quit the game properly
        pygame.quit()

if (__name__ == "__main__"):
    App()
