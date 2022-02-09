# import randint, sample functions from random module
from random import randint, sample
# import string module
import string

# define and initialize empty "dicts_list" list of dictionaries
dicts_list = []
# define and initialize empty "let_list_full" list of letters
let_list_full = []
# define and initialize empty "dict_fin" dictionary
dict_fin = {}
# final lists
list_keys_fin = []
list_values_fin = []
# borders for the number of dictionaries a, b
a = 2
b = 10
# borders for the number of letters m, n
m = 1
n = 26
# borders for the random values of numbers p, r
p = 0
r = 100


# get dictionary from two lists
def get_dict(list_of_letters, list_of_numbers):
    dict_from_lists = {}
    dict_from_lists = dict(zip(list_of_letters, list_of_numbers))
    return dict_from_lists


# get list of letters
def get_list_of_letters(cnt_letters):
    letters_list = []
    letters_list = sample(string.ascii_lowercase, cnt_letters)
    letters_list.sort()
    return letters_list


# get list of numbers
def get_list_of_numbers(cnt_letters):
    numbers_list = []
    for y in range(cnt_letters):
        numbers_list.append(randint(p, r))
    return numbers_list


# take the first element as the minimum key, after sorting
def get_min_key(dict_for_letter, max_val_for_letter):
    keys_for_max_val_dict = {k: v for k, v in dict_for_letter.items() if v == max_val_for_letter}
    min_key_for_letter = sorted(keys_for_max_val_dict.keys())[0]
    return min_key_for_letter


# define and initialize integer variable "cnt_dict" for count of dictionaries using randint function
cnt_dict = randint(a, b)
for i in range(cnt_dict):
    # define and initialize integer variable "cnt_let" for count of letters
    cnt_let = randint(m, n)

    # generate list of letters and list of numbers
    let_list = get_list_of_letters(cnt_let)
    numb_list = get_list_of_numbers(cnt_let)

    # generate dictionary from two lists "let_list"(letters) and "numb_list"(numbers)
    dicts = get_dict(let_list, numb_list)

    # generate list of all dictionaries
    dicts_list.append(dicts)
    # generate "let_list_full" list of all letters from all "let_list" lists from all dictionaries
    let_list_full.append(let_list)

# convert list of lists to list
let_list_full = sum(let_list_full, [])
# convert "let_list_full" list to list with unique letters using set() method and list() function
let_list_full = list(set(let_list_full))
# sort the "let_list_full" list in ascending order
let_list_full.sort()

# for all letters from "let_list_full" list in turn
for letter in let_list_full:
    # create a variable "key_letter" and assign it the value of received letter
    key_letter = letter
    # define and initialize empty "list_indexes" and "list_values" lists and "letter_dict" dictionary
    list_indexes = []
    list_values = []
    letter_dict = {}
    # for all dictionaries from the list in turn
    for d in range(len(dicts_list)):
        # take the dictionary from the list by index
        sep_dicts = dicts_list[d]
        # take value by key
        val = sep_dicts.get(letter, -1)
        # if value exists (not equal -1)
        if val != -1:
            # create list of dictionary numbers
            list_indexes.append(d + 1)
            # create list of values
            list_values.append(val)
            # generate dictionary from these two lists
            letter_dict = get_dict(list_indexes, list_values)
    # if the list is not empty
    if letter_dict:
        # find max value
        max_val = sorted(letter_dict.values())[-1]
        # to check if we have the same value for letter in different dictionaries take all where value equal our max_val
        # take the first element as the minimum key, after sorting
        min_key = get_min_key(letter_dict, max_val)

        # add to the name of letter '_number of dictionary' if length of "list_values" > 1
        if len(list_values) > 1:
            key_letter = f'{key_letter}_{min_key}'

        # generate a list of key letters using append() method and adding letters
        list_keys_fin.append(key_letter)
        # # generate a list of max values using append() method and adding max values
        list_values_fin.append(max_val)

        # generate final dictionary from these two lists
        dict_fin = get_dict(list_keys_fin, list_values_fin)

print(f'\nList of dictionaries:  {dicts_list}')
print(f'\nCommon dictionary:     {dict_fin}')
