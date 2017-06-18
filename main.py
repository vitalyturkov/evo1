import string
import re
from pprint import pprint
import pdb # debug
# TODO опциональные тесты


# Get a given data from a dictionary with position provided as a list
def getFromDict(dataDict, mapList):    
    for k in mapList: 
        # pdb.set_trace()
        dataDict = dataDict[k]
    return dataDict

# Set a given data in a dictionary with position provided as a list
def setInDict(dataDict, mapList, value): 
    for k in mapList[:-1]: 
        if k not in dataDict: 
            dataDict[k] = {}
        dataDict = dataDict[k]
    dataDict[mapList[-1]] = value


def optimize_data(template, data):
    pieces = []
    keys_to_use = []
    d = {}
    for piece in tuple(string.Formatter().parse(template)):
        pieces.append(piece[1])
    for piece in pieces:
        if type(piece) is type('blah'):
            keys_to_use.append( [ x for x in re.split(r'[\[\]]', piece) if x is not ''] )
            pprint(keys_to_use) # debug kinda
    for keymap in keys_to_use:
        # pdb.set_trace() # debug
        setInDict(d, keymap[:], getFromDict(data, keymap[:]))
    return d


def main():
    template = 'Python version: {languages[python][latest_version]}'
    data = {
        'languages': {
            'python': {
                'latest_version': '3.6',
                'site': 'http://python.org',
            },
            'rust': {
                'latest_version': '1.17',
                'site': 'https://rust-lang.org',
            },
        },
    }
    print("Original data:")
    pprint(data)

    new_data = optimize_data(template, data)
    print("Optimized data:")
    pprint(new_data)


if __name__ == '__main__':
    main()
