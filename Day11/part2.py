def new_password(dict_str):
    dict_str.update({8: dict_str.get(8)+1})
    for i in reversed(range(1,9)):
        if dict_str.get(i) > len(alphabet):
            dict_str.update({i: 1})
            dict_str.update({i-1: dict_str.get(i-1)+1})
        
    return dict_str

class Some_Error(BaseException):
    None

f = open('input.txt')

S = f.readline()

f.close

S = S.strip()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def PASSWORD_GENERATOR_1(s):

    dict_str = {}
    
    counter = 1
    for alpha in s:
        dict_str.update({counter: alphabet.find(alpha)+1})
        counter += 1

    values = list(dict_str.values())
    
    while True:
        try:
            if alphabet.find('i')+1 in dict_str.values() or alphabet.find('o')+1 in dict_str.values() or alphabet.find('l')+1 in dict_str.values():
                raise Some_Error()
            
            s = str()
            for i in range(1,9):
                s += alphabet[dict_str.get(i)-1]
            
            new_array = []
            counter = 1
            try:
                for i in range(len(s)):
                    if s[i] == s[i+1]:
                        counter += 1
                    else:
                        new_array.append([s[i], counter])
                        counter = 1
            except IndexError:
                new_array.append([s[i], counter])
            counter = 0
            for element in new_array:
                if element[1] > 1:
                    counter += 1
            if counter < 2:
                raise Some_Error()
            
            new_array = []
            for i in range(len(s)-2):
                new_array.append(s[i]+s[i+1]+s[i+2])
            for element in new_array:
                if element in alphabet:
                    raise ZeroDivisionError()
            raise Some_Error()
                
        except Some_Error:
            dict_str = new_password(dict_str)
        except ZeroDivisionError:
            break
    return s

def PASSWORD_GENERATOR_2(s):
    dict_str = {}
    counter = 1
    for alpha in s:
        dict_str.update({counter: alphabet.find(alpha)+1})
        counter += 1

    values = list(dict_str.values())
    dict_str = new_password(dict_str)
    s = str()
    for i in range(1,9):
        s += alphabet[dict_str.get(i)-1]
    s = PASSWORD_GENERATOR_1(s)
    return s
                                
S = PASSWORD_GENERATOR_1(S)
S = PASSWORD_GENERATOR_2(S)

f = open('output2.txt', 'w+')

print(S, file = f)

f.close
