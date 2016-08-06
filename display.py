from termcolor import cprint

RED  = 'red'
BLUE = 'blue'

def print_dictionary(dictionary):
    def print_dictionary_helper(dictionary,level):
        if isinstance(dictionary,dict):
            for key in dictionary:
                cprint(" " * level + key,BLUE)
                print_dictionary_helper(dictionary[key], level + 1)
        else:
            cprint(" " * level + dictionary, RED)

    print_dictionary_helper(dictionary, 0)
