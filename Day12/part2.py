def changer(json_file):
    if type(json_file) == list and json_file != []:
        return sum(changer(element) for element in json_file)
    elif type(json_file) == dict and 'red' in json_file.values():
        return 0
    elif type(json_file) == str:
        return 0
    elif type(json_file) == int:
        return json_file
    elif type(json_file) == dict:
        return changer(list(json_file.values()))

import json

f = open('input.txt')

S = f.readline()

f.close()

A = changer(json.loads(S))

f = open('output2.txt', 'w+')

print(str(A), file = f)

f.close()
