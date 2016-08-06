def print_dictionary(dictionary):
    def print_dictionary_helper(dictionary,level):
        if isinstance(dictionary,dict):
            for key in dictionary:
                print_dictionary(dictionary[key])
        else:
            print(" "*level+dictionary)
            
    print_dictionary_helper(dictionary,0)
