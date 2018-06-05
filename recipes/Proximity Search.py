string = "some random string some random other"
keywords = ['some','string','other']

#test consecutive  occurence of different keywords in a string

string = (i for i in string.split())

#might use tuples or generator instead of dictionary

kv = {k:v for (k,v) in enumerate(string) if v in keywords}

for key,value in kv.items():
    print(value)
    a = next( ((k,v) for k,v in kv.items() if value != v and k > key), None )
    print(a)
    
    
