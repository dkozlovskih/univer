def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [5412, 'jkldfjlg', None]
values_dict = {'a':23234, 'b':38, 'c':6875}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Denndlkcn', 98897]
print_params(*values_list_2, 42)

