class Test:
    def __init__(self, name, num, string):
        
        self.name = name

        self.string = {}
        self.string[num] = string
    def add(self, num, string):
        self.string[num] = string
        
