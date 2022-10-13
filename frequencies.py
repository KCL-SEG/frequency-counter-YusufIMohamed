"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    items = [str(i) for i in items]#convert to string
    for x in range(0,len(items)):
        #print(items[x])
        #print("This is the number of" +items[x-1] + "there are: " +str(items.count(items[x-1])))
        frequencies[items[x-1]] = items.count(items[x-1])
    return frequencies
