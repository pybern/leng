#string = "a a x x x a x x x "
string = '''random is string ok here string random , not a string. 
bahhhahhahahaha
bahhhahhahahaha
bahhhahhahahaha
this is another random string for random purposes
'''
keywords = ['random','string']

#test consecutive  occurences of different keywords in a string

_string = [i for i in string.split()]
lookup = []

#might use tuples or generator instead of dictionary

kv = [ (k,v) for (k,v) in enumerate(_string) if v in keywords ]
print(kv,'\n')


for key,value in kv:
    a = next( ( (key,k)  for k,v in kv if key < k < key+5) , None )

    if a is not None:
        lookup.append(a)
    print(lookup)
        
print('\n',lookup,'\n\n',string)

chains = []
chain = []

for i in lookup:
    a = next( (i[1] for key in lookup if key[1] == i[0]) , None)
    
    if a is None:
        if chain:
            chains.append(chain)
        chain = []
        chain.append(i[0])
        
    else:
        if len(chain) == 1:
            chain.append(a)
        else:
            chain[1] = a
        
chains.append(chain)
        
    
print(lookup,'\n\n',chains)

for i in chains:
    print(' '.join( _string[i[0]:i[1]+1] ) )
