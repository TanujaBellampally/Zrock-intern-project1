# Write a Python program to find the keys in a dictionary.
def key(d,v):
    for keys,values in d.items():
        if(values==v):
            print( keys)
        
v=input()        
d={"1":"f","2":"d","3":"r","5":"h" }
key(d,v)