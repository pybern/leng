#string = "a a x x x a x x x "

#test consecutive  occurences of different keywords in a string
    
def build_lookup(string, keywords):
    _string = [i for i in string.lower().split()]
    lookup = []

    #might use tuples or generator instead of dictionary

    kv = [ (k,v) for (k,v) in enumerate(_string) if v in keywords ]
    
    for key,value in kv:
        a = next( ( (key,k)  for k,v in kv if key < k < key+5) , None )

        if a is not None:
            lookup.append(a)
            print(key,value,lookup)

    return(lookup)
    print(lookup)


#manage here to, multilookup

def build_chain(lookup):
    chains = []
    chain = []

    for i in lookup:
        if len(lookup) == 1:
            chain.extend(i)

        else:
            a = next( (i[1] for key in lookup if key[1] == i[0]) , None)

            if a is None:
                if len(chain) > 1:
                    chains.append(chain)
                chain = []
                chain.append(i[0])

            else:
                if len(chain) == 1:
                    chain.append(a)
                else:
                    chain[1] = a
    
    chains.append(chain)
    
    print(chains)
    return(chains)
    


def preview(string,chains):
    for i in chains:
        _string = [i for i in string.lower().split()]
        start = i[0] - 10  if i[0] > 10 else i[0]
        end = i[1]+11 if i[1]+1 < 10 else i[1]+1 
        print(' '.join( _string[i[0]:i[1]+1] ) )
        
string = ''' This is our world now... the world of the electron and the switch , the
beauty of the baud .  We make use of a service already existing without paying
for what could be dirt-cheap if it wasn't run by profiteering gluttons, and
you call us criminals.  We explore... and you call us criminals.  We seek
after knowledge... and you call us criminals.  We exist without skin color,
without nationality, without religious bias... and you call us criminals.
You build atomic bombs, you wage wars, you murder, cheat, and lie to us
and try to make us believe it's for our own good, yet we're the criminals.'''

#keywords = input().split()
keywords = ['electron','world']
