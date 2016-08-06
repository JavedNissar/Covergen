import json

def parse_argument(argument):
    arguments = argument.split('.')
    name = arguments[-1]
    clarifiers = arguments[:-1]
    return clarifiers,name

def get_dictionary(clarifiers,dictionary,create_dictionary = False):
    if clarifiers == []:
        return dictionary

    current_dictionary = dictionary

    for clarifier in clarifiers:
        if clarifier in current_dictionary:
            current_dictionary = current_dictionary[clarifier]
        elif create_dictionary:
            current_dictionary[clarifier] = {}
            current_dictionary = current_dictionary[clarifier]

    return current_dictionary

def get_from_dictionary(argument,dictionary,create_dictionary = False):
    clarifiers, name = parse_argument(argument)

    current_dictionary = get_dictionary(clarifiers, dictionary,create_dictionary)

    return current_dictionary[name]

def insert_into_dictionary(argument,sentence,dictionary,create_dictionary = False):
    clarifiers, name = parse_argument(argument)

    current_dictionary = get_dictionary(clarifiers, dictionary,create_dictionary)

    current_dictionary[name] = sentence

def update_json_file(data,open_file):
    file_data = open_file.read()
    open_file.seek(0)
    open_file.write(json.dumps(data))
    open_file.truncate()
