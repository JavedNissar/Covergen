import add
from exceptions import ParseError

def get_lines(file):
    lines = file.readlines()
    import_lines = []
    text_lines = []

    for line in lines:
        if line.split(' ')[0] == 'import':
            import_lines.append(line)
        elif not line.startswith('#'):
            text_lines.append(line)

    return import_lines,text_lines

def parse_import_lines(import_lines):
    names_table = {}
    for index,line in enumerate(import_lines):
        line = line.strip()
        split_line = line.split(' ')
        line_index = index + 1

        if split_line[0] != 'import':
            raise ParseError("import keyword not found",line_index)

        if split_line[1] in names_table.values():
            raise ParseError("Duplicate import statement found",line_index)

        if len(split_line) > 2:
            if split_line[2] != 'as':
                raise ParseError("as keyword not found",line_index)

            if split_line[3] in names_table:
                raise ParseError("Duplicate name found",line_index)

            names_table[split_line[3]] = split_line[1]
        else:
            names_table[split_line[1]] = split_line[1]

    return names_table

def get_dictionary(clarifiers,root_dir,line_number):
    for index,dirName,subDirList,fileList,clarifier in enumerate(zip(os.walk(root_dir),clarifiers)):
        if index == len(clarifiers) - 1:
            for fname in fileList:
                if clarifier in fname:
                    if fname.endswith('.json'):
                        return json.load(open(fname))
                    else:
                        raise ParseError('Import was not JSON file',line_number)
        for index in range(len(subDirList)):
            if subDirList[index] != clarifier:
                del subDirList[index]
    raise ParseError('Import not found',line_number)

def get_dictionaries(names_table,data):
    library_table = {}
    for name in names_table:
        data_name = names_table[name]
        split_name = data_name.split('.')
        current_dictionary = get_dictionary(split_name, data)
        if not isinstance(current_dictionary,dict):
            raise TypeError("Name found is not a dictionary")
        library_table[name] = current_dictionary
    return library_table

def parse_text_lines(text_lines,library_table):
    text = ''.join(text_lines)
    compiled_text = text.format(**library_table)
    return compiled_text
