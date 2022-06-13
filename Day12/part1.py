f = open('input.txt')

S = f.readline()

f.close()

S = string.replace(' ', '')

for element in S:
    if element.isdigit() == False and element != '-':
        S = S.replace(element, '.')

A = []
B = []
A = S.split('.')

for element in A:
    if element != '':
        B.append(int(element))

f = open('output1.txt', 'w+')

print(str(sum(B)), file = f)

f.close()
