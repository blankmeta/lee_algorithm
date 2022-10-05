buttons_per_string = 5
buttons_per_column = 5

if __name__ == '__main__':
    array = [[1 for str_bt in range(buttons_per_string)]
             for cl_bt in range(buttons_per_column)]
    print(array)
