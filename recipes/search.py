string = "some random string some random other"
keywords = ['some','string','other']

#test consecutive  occurence of different keywords in a string
#lookup creates a graph styled network to trace the distance of words

string = (i for i in string.split())
lookup = []

#might use tuples or generator instead of dictionary

kv = {k:v for (k,v) in enumerate(string) if v in keywords}
print(kv,'\n')


for key,value in kv.items():
    a = next( ( (key,k,value,v)  for k,v in kv.items() if key < k < key+5) , None )
    if a is not None:
        lookup.append(a)
    print('{}'.format( (key,value) ))
    
