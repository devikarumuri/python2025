#FUNCTIONS
#add functions
def add():
    num_1=10
    num_2=20
    print(num_1+num_2)
add()

#square function
def square(a):
    return a*a
number=int(input("enter the number:"))
obj=square(number)
print(f"square of the given number is {obj}")

#factorial function
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter the number for factorial"))
obj=factorial(n)
print(f"the factorial of {n} is {obj}")

#maximum function
def maximum():
    num_1=int(input("enter the number:"))
    num_2=int(input("enter the number:"))
    num_3=int(input("enter the number"))
    import math
    findingmax=max(num_1,num_2,num_3)
    print(findingmax)
maximum()

#reverse function
def reverse(string):
    return string[::-1]
user=input("enter the string to be reversed:")
reversed=reverse(user)
print(f"the given string reversed is{reversed}")

#prime or not
def prime(number):
    number=int(number)
    if number>1:
        for digit in range(2,number):
            if(number%digit==0):
                print(f"{number} is prime")
                return False
            else:
                print(f"{number} is prime")
                return True
prime(11)

#fibonacci
def fibanacci(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
fibanacci(10)

#palindrome
def palindrome(s):
    return s==s[::-1]
s=input("Enter a string:")
if palindrome(s):
    print("It is a palindrome")
else:
    print("It is not a palindrome")


        
