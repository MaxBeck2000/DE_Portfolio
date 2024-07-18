def cleanup_address_book(address_book):
    new_ab = {}
    for k, v in address_book.items():
        name = k.split()
        v = f"{v}"
        if len(name) == 1:
            fname = name[0].capitalize()
            if len(v) > 7:
                v1 = v[0:-6] + " " + v[-6:] 
                new_ab[fname] = v1
            else:
                new_ab[fname] = v
        if len(name) == 2:
            fname = name[0].capitalize()
            lname = name[1].capitalize()
            if len(v) > 7:
                v1 = v[0:-6] + " " + v[-6:]
                new_ab[fname + " " + lname] = v1
            else:
                new_ab[fname + " " + lname] = v
    return new_ab


def search_address_book(address_book, search_string):
    address_book_filtered = {}
    for name in address_book:
        if name.lower().find(search_string.lower()) == 0:
            address_book_filtered[name] = address_book[name]

    return address_book_filtered


def count_vowels(input_string):
    vowel_count = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for vowel in vowel_count:
        vowel_count[vowel] = input_string.lower().count(vowel)
    return vowel_count


def get_names_in_common(address_book1, address_book2):

    names_1 = set(address_book1.keys())
    names_2 = set(address_book2.keys())
    names_in_common = names_1.intersection(names_2)
    return names_in_common


def get_numbers_in_common(address_book1, address_book2):
    my_set = set()
    a = list(address_book1.values())
    b = list(address_book2.values())
    for i in a:
        if i in b:
            my_set.add(f"{i}")
    return my_set


def combine_address_books(address_book1, address_book2):
    my_dict = {}
    my_dict2 = {}
    set1 = set(address_book1)
    for k, v in address_book1.items():
        my_dict[k] = v
    for k, v in address_book2.items():
        if k not in set1:
            my_dict[k] = v
        else:
            my_dict2[k] = v
    my_tuple = (my_dict, my_dict2)
    return my_tuple
