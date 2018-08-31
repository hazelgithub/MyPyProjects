import numpy as np
#import pandas as pand

arr = np.array([1,2,3,4])
print('array is',arr)

print("Welcome To Calculator")

def add(num1,num2):
    sum = num1 + num2
    return sum

def sub(num1,num2):
    sub = num1 - num2
    return sub

def mult(num1,num2):
    return (num1 * num2)

def div(num1,num2):
    return (num1/num2)


a = 'i am learning Python, what about you !!!'
b = a.split(' ')
## Enhancing for Release 2
# Branch rel2
#print (len(b))

print (b)
i = 0
while i < len(b):
    print (b[i])
    i = i + 1

## Adding HotFix rel1.1
## Enhancing for Release 1
# Branch rel1
print ('########## {} ##########').format('Enhancement for Release 1')
print(add(5,10))

## Adding HotFix rel1.1
## Enhancing for Release 2
# Branch rel2
print ('########## {} ##########').format('Enhancement for Release 2')
print(sub(15,2))
