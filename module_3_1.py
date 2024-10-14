calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(str):
    count_calls()
#    str = input('введите строку:')
    str0 = len(str)
    str1 = str.lower()
    str2 = str.upper()
    return(str0, str1, str2)


def is_contains(str, list_):
    count_calls()
    for k in list_:
        if str.lower() == k.lower():
            return True
    return False


print(string_info('kkjdhfkagwkfjwek;fhkwjfhw'))
print(string_info('dnjkjkkjgakfgkj'))
print(string_info('jbfbje'))
print(is_contains('Denis', ['gsd', 'fgf', 'Denis']))
print(is_contains('DENIS', ['fgfh', 'sd', 'hfsh', 'kjhk']))
print(is_contains('fgfh', ['fgFh', 'sd', 'hfsh', 'kjhk']))
print(calls)