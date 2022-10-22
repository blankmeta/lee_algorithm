from pprint import pprint

BUTTONS_PER_STRING = 5
BUTTONS_PER_COLUMN = 5



if __name__ == '__main__':
    array = [[str_bt for str_bt in range(buttons_per_string)]
             for cl_bt in range(buttons_per_column)]
    pprint(array)
    print(array[0][2])
