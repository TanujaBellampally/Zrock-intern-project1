# Write a Python program to find the index of an element in a list. 
def fin(e,l):
    for i in range(len(l)):
        if(e==l[i]):
            p=i
            break
    return p
            
        
    
    
    
    
    
    
l=[int(x) for x in input().split(" ")]
e=int(input())
print(fin(e,l))