import json

resource_file = open('resources/data.json')
dictionary = dict(json.load(resource_file))


def translate(word: str) -> list:
    """
    Return the meaning of the specific word that exist in the dictionary
    :param word: The look-up word
    :type word: str
    :return: the translations of the specific word
    :rtype: list
    """
    return dictionary.get(word.lower(), f'The word "{word}" does not exist in the dictionary!')


def report(meanings):
    if type(meanings) is list:
        for index, meaning in enumerate(meanings):
            print(f'{index+1}: {meaning}')
    else:
        print(meanings)
    print()


while True:
    input_word = input('Enter word: ')
    report(translate(input_word))
