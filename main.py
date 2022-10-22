from pprint import pprint

import pygame
from typing import List

from config import BUTTONS_PER_STRING, BUTTONS_PER_COLUMN

pygame.init()
screen = pygame.display.set_mode((750, 750))
screen.fill('white')
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

colors = ['grey', 'black', 'red', 'green']

color_to_char = {
    colors[0]: '-',
    colors[1]: 'X',
    colors[2]: 's',
    colors[3]: 'f'
}


class Button:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, pos, bg='black', feedback=''):
        self.x, self.y = pos
        self.size = (100, 100)
        self.font = font
        self.surface = pygame.Surface(self.size)
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.bg = bg
        self.surface.fill(bg)

        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback

    def change_status(self, bg="black"):
        """Change the color what you click"""
        self.bg = bg
        self.surface.fill(bg)

    def change_text(self, text: str) -> None:
        text = self.font.render(text, True, pygame.Color("White"))
        self.surface.blit(text, (0, 0))

    def show(self):
        screen.blit(self.surface, (self.x, self.y))

    def clean(self):
        self.change_status(bg=colors[0])
        self.change_text('')

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    print(x, y)
                    color_index = colors.index(self.bg)
                    color_index += 1
                    if color_index == len(colors):  # the last color
                        color_index = 0
                    self.change_status(bg=colors[color_index])

    def __str__(self):
        return f'{self.x}:{self.y}'

    def __repr__(self):
        return f'{self.x}:{self.y}'


def clean(buttons: List[List[Button]]) -> None:
    for line_count, line in enumerate(buttons):
        for values_count, bt in enumerate(buttons):
            buttons[line_count][values_count].clean()


def buttons_to_array(buttons: List[List[Button]]) -> List[list]:
    result = []
    for line in buttons:
        new_line = [color_to_char[another_bt.bg] for another_bt in line]
        result.append(new_line)
    return result


def array_to_buttons(array: List[list], buttons: List[List[Button]]) -> None:
    for line_count, line in enumerate(array):
        for values_count, value in enumerate(line):
            buttons[line_count][values_count].change_text(str(value))


def build_lee(array: List[list], dot_coords: List[int]):
    if array[dot_coords[0]][dot_coords[1]] == 's':
        number = 0
    else:
        number = array[dot_coords[0]][dot_coords[1]]

    # up
    if (dot_coords[0] - 1) >= 0:
        if (array[dot_coords[0] - 1][dot_coords[1]]) == '-':
            array[dot_coords[0] - 1][dot_coords[1]] = number + 1

    # right
    if (dot_coords[1] + 1) < BUTTONS_PER_STRING:
        if (array[dot_coords[0]][dot_coords[1] + 1]) == '-':
            array[dot_coords[0]][dot_coords[1] + 1] = number + 1

    # left
    if (dot_coords[1] - 1) >= 0:
        if (array[dot_coords[0]][dot_coords[1] - 1]) == '-':
            array[dot_coords[0]][dot_coords[1] - 1] = number + 1

    # down
    if (dot_coords[0] + 1) < BUTTONS_PER_COLUMN:
        if (array[dot_coords[0] + 1][dot_coords[1]]) == '-':
            array[dot_coords[0] + 1][dot_coords[1]] = number + 1

    return array


def lee(array: List[list]) -> List[list]:
    start_coords = []
    status = 0
    for line_count, line in enumerate(array):
        for char_count, char in enumerate(line):
            if char == 's':
                start_coords = [line_count, char_count]
    for i in range(8):
        status_coords = []
        if status == 0:
            array = build_lee(array, start_coords)
            # pprint(array)
        else:
            for line_count, line in enumerate(array):
                for char_count, char in enumerate(line):
                    if char == status:
                        status_coords.append([line_count, char_count])
            for coords in status_coords:
                array = build_lee(array, coords)
                # pprint(array)
        status += 1
    return array


def mainloop():
    """ The infinite loop where things happen """
    lee_status = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                try:
                    if event.key == pygame.K_SPACE:
                        clean(buttons)
                    if event.key == pygame.K_RIGHT:
                        array = buttons_to_array(buttons)
                        pprint(array)
                        array = lee(array)
                        pprint(array)
                        array_to_buttons(array, buttons)
                except IndexError:
                    print('Fill the space')
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


buttons = [[Button(
    # (str_bt * 101, cl_bt * 101),
    (str_bt * 101, cl_bt * 101),
    bg=colors[0],
    feedback="You clicked me")
    for str_bt in range(BUTTONS_PER_STRING)]
    for cl_bt in range(BUTTONS_PER_COLUMN)]

if __name__ == '__main__':
    console_info()
    mainloop()
