from pprint import pprint

BUTTONS_PER_STRING = 30
BUTTONS_PER_COLUMN = 30

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800

DELAY = 0.25

if __name__ == '__main__':
    array = [[str_bt for str_bt in range(buttons_per_string)]
             for cl_bt in range(buttons_per_column)]
    pprint(array)
    print(array[0][2])
