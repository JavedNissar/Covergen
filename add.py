def parse_argument(argument):
    arguments = argument.split('.')
    name = arguments[-1]
    clarifiers = arguments[:-1]
    return clarifiers,name

def get_dictionary(clarifiers,dictionary):
    current_dictionary = dictionary
    for clarifier in clarifiers:
        current_dictionary = current_dictionary[clarifier]

    return current_dictionary

def get_from_dictionary(argument,dictionary):
    clarifiers, name = parse_argument(argument)

    current_dictionary = get_dictionary(clarifiers, dictionary)

    return current_dictionary[name]

def insert_into_dictionary(argument,sentence,dictionary):
    clarifiers, name = parse_argument(argument)

    current_dictionary = get_dictionary(clarifiers, dictionary)

    current_dictionary[name] = sentence
