from pprint import pprint

import pygame

from config import buttons_per_string, buttons_per_column

pygame.init()
screen = pygame.display.set_mode((750, 750))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)


class Button:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, pos, bg="black", feedback=""):
        self.x, self.y = pos
        self.size = (100, 100)
        self.surface = pygame.Surface(self.size)
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.surface.fill(bg)

        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        # self.change_text(text, bg)

    def change_status(self, bg="black"):
        """Change the color what you click"""
        self.surface.fill(bg)

    def show(self):
        screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    print(x, y)
                    self.change_status(bg="red")

    def __str__(self):
        return f'{self.x}:{self.y}'

    def __repr__(self):
        return f'{self.x}:{self.y}'


def mainloop():
    """ The infinite loop where things happen """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            for st in buttons:  # returns list
                for button in st:
                    button.click(event)
        for st in buttons:  # returns list
            for button in st:
                button.show()
        clock.tick(30)
        pygame.display.update()


def console_info():
    print(f'Всего полей:\n{sum(len(lst) for lst in buttons)}')
    pprint(buttons)


array = [[1 for str_bt in range(buttons_per_string)]
         for cl_bt in range(buttons_per_column)]

buttons = [[Button(
    (str_bt * 101, cl_bt * 101),
    bg="navy",
    feedback="You clicked me")
    for str_bt in range(buttons_per_string)]
    for cl_bt in range(buttons_per_column)]

if __name__ == '__main__':
    console_info()
    mainloop()
