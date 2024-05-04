# Write a Python program to find a substring in a string. 
def sub(s,su):
  l=len(su)  
  for i in range(len(s)):
      
    sp=s[i:l+i]
    
    if(su==sp):
        return su
    else:
        continue
    
    
    
    
s=input()
su=input()
print(sub(s,su))