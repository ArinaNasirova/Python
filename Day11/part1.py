def new_password(dict_str):
    dict_str.update({8: dict_str.get(8)+1})
    for i in reversed(range(1,9)):
        if dict_str.get(i) > len(alphabet):
            dict_str.update({i: 1})
            dict_str.update({i-1: dict_str.get(i-1)+1})
        
    return dict_str

class Some_Error(BaseException):
    None

alphabet = 'abcdefghijklmnopqrstuvwxyz'
dict_str = {}

f = open('input.txt')

S = f.readline()

f.close

S = S.strip() 

counter = 1
for alpha in S:
    dict_str.update({counter: alphabet.find(alpha)+1})
    counter += 1

values = list(dict_str.values())

while True:
    try:
        if alphabet.find('i')+1 in dict_str.values() or alphabet.find('o')+1 in dict_str.values() or alphabet.find('l')+1 in dict_str.values():
            raise Some_Error()
        
        S = str()
        for i in range(1,9):
            S += alphabet[dict_str.get(i)-1]
            
        new_array = []
        counter = 1
        try:
            for i in range(len(S)):
                if S[i] == S[i+1]:
                    counter += 1
                else:
                    new_array.append([S[i], counter])
                    counter = 1
        except IndexError:
            new_array.append([S[i], counter])
        counter = 0
        for element in new_array:
            if element[1] > 1:
                counter += 1
        if counter < 2:
            raise Some_Error()
        
        new_array = []
        for i in range(len(S)-2):
            new_array.append(S[i]+S[i+1]+S[i+2])
        for element in new_array:
            if element in alphabet:
                raise ZeroDivisionError()
        raise Some_Error()
                
    except Some_Error:
        dict_str = new_password(dict_str)
    
    except ZeroDivisionError:
        break

f = open('output1.txt', 'w+')

print(S, file = f)

f.close
