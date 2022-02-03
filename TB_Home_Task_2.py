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

try:
    # define and initialize integer variable "cnt_dict" for count of dictionaries using randint function
    cnt_dict = randint(2, 10)
    # for each dictionary in a loop from 0 to cnt_dict
    for i in range(cnt_dict):
        # define and initialize integer variable "cnt_let" for count of
        # letters using randint function from random module
        cnt_let = randint(1, 26)
        # define and initialize "let_list" list of "cnt_let" lowercase letters using
        # 1. the "ascii_lowercase" string constants from string module to get string of letters
        # 2. the "sample" method from random module to get "cnt_let" of them
        let_list = sample(string.ascii_lowercase, cnt_let)
        # sort the "let_list" list in ascending order (for easy checking later)
        let_list.sort()

        # define and initialize empty "numb_list" list of numbers for dictionary.
        numb_list = []
        # for each dictionary in a loop from 0 to "cnt_let"
        for cnt in range(cnt_let):
            # generate a list of numbers for dictionary using append() method
            # that add random element (number from 0 to 100) to the end of the list.
            # The amount of numbers is the same as the number of letters for a particular dictionary.
            numb_list.append(randint(0, 100))

        # define and initialize empty "dicts" dictionary of letters as a key and numbers as an element.
        dicts = {}
        # generate dictionary from two lists "let_list"(letters) and "numb_list"(numbers)
        # using zip() function and dict() function
        dicts = dict(zip(let_list, numb_list))
        # generate list of all dictionaries
        dicts_list.append(dicts)

        # generate "let_list_full" list of all letters from all "let_list" lists from all dictionaries
        for j in range(len(let_list)):
            let_list_full.append(let_list[j])

    # convert "let_list_full" list to list with unique letters using set() method and list() function
    let_list_full = list(set(let_list_full))
    # sort the "let_list_full" list in ascending order
    let_list_full.sort()
    # display the "dicts_list" list
    print(f'\nList of dictionaries:  {dicts_list}')

    # define and initialize empty "list_keys_fin" and "list_values_fin" lists
    list_keys_fin = []
    list_values_fin = []

    # for all letters from "let_list_full" list in turn
    for ll in range(len(let_list_full)):
        # take the letter from the list by index
        letter = let_list_full[ll]
        # create a variable "key_letter" and assign it the value of received letter
        key_letter = letter

        # define and initialize empty "list_indexes" and "list_values" lists
        list_indexes = []
        list_values = []

        # for all dictionaries from "dicts_list" list in turn
        for d in range(len(dicts_list)):
            # take the dictionary from the list by index
            sep_dicts = dicts_list[d]
            # take value by key(letter) using get() method and assign to val variable.
            # If the key(letter) is missing, it will return the default value = -1
            val = sep_dicts.get(letter, -1)
            # if value exists (not equal -1)
            if val != -1:
                # generate "list_indexes" list (sequence number of the dictionary)
                # and "list_values" list of values for letter
                list_indexes.append(d + 1)
                list_values.append(val)
                # generate dictionary from two lists "list_indexes" and "list_values"
                letter_dict = dict(zip(list_indexes, list_values))
        # find max value using values() method to find values from dictionary and
        # sorted() method to sort them and take last element as the maximum
        max_val = sorted(letter_dict.values())[-1:]
        # convert the content of a list variable to an integer
        max_val = int(max_val[0])
        # to check if we have the same value for letter in different dictionaries take all where value equal our max_val
        keys_for_max_val = {k: v for k, v in letter_dict.items() if v == max_val}
        # take the first element as the minimum key, after sorting
        min_key = sorted(keys_for_max_val.keys())[0]
        # add to the name of letter '_number of dictionary' if length of "list_values" > 1
        if len(list_values) > 1:
            # redefine key_letter variable
            key_letter = key_letter + '_' + str(min_key)

        # generate a list of key letters using append() method and adding letters
        list_keys_fin.append(key_letter)
        # generate a list of key letters using append() method and adding max values
        list_values_fin.append(max_val)
        # generate final dictionary from two lists
        dict_fin = dict(zip(list_keys_fin, list_values_fin))
    # display the "dict_fin" dictionary
    print(f'\nCommon dictionary:     {dict_fin}')
except:
    print('\nSome error has occurred')
