import os
import json

class ParseError(Exception):
    def __init__(self,value,index):
        self.index = index
        self.text = value
    def __str__(self):
        return (self.text +
        " at line {index} in the file you're compiling"
        .format(index=self.index))

def get_lines(coverletter_file):
    """
    Get the text and import lines of a coverletter template

    file coverletter_file: An open file
    rtype: ([str],[str])
    """
    lines = coverletter_file.readlines()
    import_lines = []
    text_lines = []

    for line in lines:
        if '#' in line:
            line = line[:line.index('#')] + '\n'

        if line.split(' ')[0] == 'import':
            import_lines.append(line)
        #any line that doesn't have import at the beginning or # is a text line
        #NOTE:The avoidance of lines with # at the beginning is to facilitate
        #comments
        elif not line.startswith('#'):
            text_lines.append(line)

    return import_lines,text_lines

def parse_import_lines(import_lines):
    """
    Parse the import lines to produce a table mapping names to statements which
    indicate the JSON file to import

    [str] import_lines:A list of the lines related to imports
    rtype: {str:(str,int)}
    """
    names_table = {}
    for index,line in enumerate(import_lines):
        line = line.strip()
        split_line = line.split(' ')
        #the addition of 1 is to have the first line be line 1 instead of line 0
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

            #create a tuple with the import statement and the line number
            #the line number is used to make finding errors easier for the user
            names_table[split_line[3]] = (split_line[1],line_index)
        else:
            names_table[split_line[1]] = (split_line[1],line_index)

    return names_table

def get_dictionary(clarifiers,root_dir,line_number):
    """
    Return a dictionary containing the data obtained from a position detailed
    by clarifiers

    [str] clarifiers:The list of directories that lead to the JSON file to be
    imported
    str root_dir:The root directory
    int line_number:The line number that the JSON file is imported at
    rtype:{str:str}
    """
    try:
        #use the root directory to make the opening file path independent
        #of the covergen script's location
        return json.load(open('/'.join([root_dir] + clarifiers)+'.json'))
    except FileNotFoundError:
        raise ParseError('Import not found',line_number)
    except json.decoder.JSONDecodeError:
        raise ParseError('Import is not valid JSON',line_number)

def get_dictionaries(names_table,root_dir):
    """
    Get all dictionaries referenced in the imports that are in the names_table

    {str,str} names_table:A dictionary mapping names to imports
    str root_dir:The root directory
    rtype:{str:{str:str}}
    """
    #library_table maps from names to dictionaries that can be construed
    #as libraries of names which map to statements
    library_table = {}
    for name in names_table:
        data_tuple = names_table[name]
        split_name = data_tuple[0].split('.')
        current_dictionary = get_dictionary(split_name, root_dir, data_tuple[1])
        library_table[name] = current_dictionary
    return library_table

def parse_text_lines(text_lines,library_table):
    """
    Compile the text present in text_lines using the library_table

    [str] text_lines:Lines of uncommented text from the cover letter template
    {str:str} library_table:A table mapping names to libraries
    rtype:str
    """
    text = ''.join(text_lines)
    compiled_text = text.format(**library_table)
    return compiled_text
