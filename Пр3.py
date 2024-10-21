def remove_duplicates(input_list):
    return list(dict.fromkeys(input_list))

input_list = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']

def sort_list(input_list):
    numbers = [x for x in input_list if isinstance(x, (int, float))]
    strings = [x for x in input_list if isinstance(x, str)]

    numbers.sort()
    strings.sort(key=lambda x: x.lower())  
    return numbers + strings

unique_list = remove_duplicates(input_list)
sorted_list = sort_list(unique_list)

print(sorted_list)
