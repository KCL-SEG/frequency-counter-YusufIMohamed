"""Frequencies function."""

def frequencies(items):
    frequencies = {}
    items = [str(i) for i in items]#convert to string
    for x in range(0,len(items)):
        frequencies[items[x-1]] = items.count(items[x-1])
    return frequencies
