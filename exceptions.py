class ParseError(Exception):
    def __init__(self,value,index):
        self.index = index
        self.text = value
    def __str__(self):
        return self.text + " at "+"line {index} in the file you're compiling".format(index=self.index)
