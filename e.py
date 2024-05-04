# Write a Python program that uses an if-elif-else statement to check if a number is positive, 
# negative, or zero. 
def check(n):
    if(n>0):
        return "positive"
    elif(n<0):
        return "negative"
    else:
        return "zero"
n=int(input())
print(check(n))