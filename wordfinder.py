"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, path):
        self.path = path
        self.word = self.parse
        
    def __repr__(self):
        return f"<The path is = {self.path}>"

    def parse(self):
       list =[]
       o = open(self.path, "r")
       for each in o:
           list.append(each.strip())
       print (f"There are {len(open(self.path).readlines())} words in this file")
       return list
    
    def random(self):
        return (random.choice(self.parse()))