import add
from exceptions import ParseError

def get_lines(file):
    lines = file.readlines()
    separator_line = lines.index('\n')
    return lines[:separator_line],lines[separator_line + 1:]

def parse_import_lines(import_lines):
    names_table = {}
    for line,index in enumerate(import_lines):
        split_line = line.split(' ')
        line_index = index + 1

        if split_line[0] == 'import':
            raise ParseError("import keyword not found",line_index)

        if split_line[1] in names_table.values():
            raise ParseError("Duplicate import statement found",line_index)

        if len(split_line) > 2:
            if split_line[2] == 'as':
                raise ParseError("as keyword not found",line_index)

            if split_line[3] in names_table:
                raise ParseError("Duplicate name found",line_index)

            names_table[split_line[3]] = split_line[1]
        else:
            names_table[split_line[1]] = split_line[1]

    return names_table

def get_dictionaries(names_table,data):
    names_table_with_dict = {}
    for name in names_table:
        data_name = names_table[name]
        split_name = data_name.split('.')
        current_dictionary = add.get_dictionary(split_name, data)
        if not isinstance(current_dictionary,dict):
            raise TypeError("Name found is not a dictionary")
        names_table_with_dict[name] = (data_name,current_dictionary)

def parse_text_lines(text_lines,library_table):
    compiled_lines = []
    for line in text_lines:
        split_line = line.split(' ')
        compiled_line = []
        for word in split_line:
            if word[0] == '/' and word[-1] == '/':
                #last index of .;used to separate the name for the library from the name of the sentence
                last_index = word.rfind('.')
                library = word[:last_index]
                name = word[last_index + 1:]
                sentence = library_table[library][name]
                compiled_line.append(sentence)
            else:
                compiled_line.append(word)
        compiled_lines.append(' '.join(compiled_line))
    return compiled_lines
