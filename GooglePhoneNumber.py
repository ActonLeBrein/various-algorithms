# Script text here

def phonenumber(s):
    n = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], 
         '5':['j','k','k'], '6':['m','n','o'], '7':['p','q','r','s'],
         '8':['t','u','v'], '9':['w','x','y','z']}
    l = str(s)
    d = ['']
    l = l.replace('1','')
    l = l.replace('0','')
    for char in l:
        letters = n.get(char, '')
        d = [prefix+letter for prefix in d for letter in letters]
    print d, len(d)

phonenumber(83766422)

def phonenumber(s):
    n = {'1':['a','b','c'], '2':['d','e','f'], '3':['g','h','i'], 
         '4':['j','k','l'], '5':['m','n','o'], '6':['p','q','r'],
         '7':['s','t','u'], '8':['v','w','x'], '9':['y','z'], '0':['_']}
    l = str(s)
    d = ['']
    for char in l:
        letters = n.get(char, '')
        d = [prefix+letter for prefix in d for letter in letters]
    return d

print phonenumber(32445)