def get_num_words(string):
    num_words = len(string.split())

    return num_words


def char_appearances(string):
    list_of_chars = list(string.lower())
    set_of_chars = set(list_of_chars)

    char_appearances = 0
    dict_of_chars = {}
    char_info = {}

    for char in set_of_chars:
        for item in list_of_chars:
            if item == char:
                char_appearances += 1
                char_info = {char : char_appearances}
        dict_of_chars.update(char_info)
        char_info.clear()
        char_appearances = 0

    return dict_of_chars

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    new_list = []
    result_list = ''

    for item in dict:
        if item.isalpha():
            new_list.append({"char": item, "num": dict[item]})

    new_list.sort(reverse=True, key=sort_on)

    for item in new_list:
        if result_list != '':
            result_list += '\n'
        str_key = item["char"]
        str_value = str(item["num"])
        result_list += str_key + ': ' + str_value

    return result_list