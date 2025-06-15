#advanced functions
#square of numbers
def square(numbers):
    return list(map(lambda x:x**2,numbers))
print(square([1,2,3,4]))

#filter_positive numbers
def filter_positive(numbers):
    return list(filter(lambda x:x>0,numbers))
print(filter_positive([-2,0,3,-1,5]))

#factorial
from functools import reduce
def calculate_factorial(n):
    return reduce(lambda x,y:x*y,range(1,n+1))
num=int(input("enter the number:"))
if num>0:
    print(f"fact of {num},is {calculate_factorial(num)}")
else:
    print("enter the correct number")

#vowel string
string=input("enter the string for vowel check:")
vowels=('a','e','i','o','u','A','E','I','O','U')
count=lambda string:sum(1 for char in string.lower() if char is vowels)
print(count(string))
