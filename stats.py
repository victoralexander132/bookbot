def get_words_count(text):
    return len(text.split())


def get_character_count(text):
    counter = {}
    text = text.lower()
    for character in text:
        if character in counter:
            counter[character] += 1
        else:
            counter[character] = 1
    return counter


def sort_on(items):
    return items["num"]


def sort_dictionary(dictionary):
    sorted_dictionary = []

    for key in dictionary.keys():
        sorted_dictionary.append({"character": key, "num": dictionary[key]})
    sorted_dictionary.sort(reverse=True, key=sort_on)
    return sorted_dictionary
