import pygame

class Button:
    """
    Create a Button, then blit the surface in the while loop
    """
    def __init__(self, screen, text, position, dimension, button_color, text_color, font):
        self.screen = screen
        self.text = text
        self.x = position[0]
        self.y = position[1]
        self.width = dimension[0]
        self.height = dimension[1]
        self.button_color = button_color # a tuple, for example: (255, 255, 255)
        self.text_color = text_color
        self.font = pygame.font.SysFont("Arial", font)

    def show(self):

        # draw the rectangle for the button
        pygame.draw.rect(self.screen, self.button_color, [self.x, self.y, self.width, self.height])

        # create the text
        text = self.font.render(self.text, True, self.text_color)

        # blit the surface
        self.screen.blit(text, (self.x + 10, self.y + 10))

    def click(self, event):
        """
        Return true when the button is clicked, otherwise false.
        (No Animation as of now)
        """
        # get the position of the mouse
        x, y = pygame.mouse.get_pos()

        # if the mouse button down is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if (self.x <= x <= self.x + self.width) and (self.y <= y <= self.y + self.height):
                    return True