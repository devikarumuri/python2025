#vowelchecker
char=input("enter the char:")
vowels=("a e i o u A E I O U")
if char in vowels:
    print(f"{char} is an vowel")
else:
    print(f"{char} is not a vowel")

#age group classification
age=int(input("enter the age:"))
if age>=0 and age<=12:
    print(f"{age} year's is child")
elif age>=13 and age<=17:
    print(f"{age} year's is teenager")
elif age>=18 and age<=64:
    print(f"{age} year's is adult")
else:
    print(f"{age} year's is senior")

# +/-/0 checking
num=int(input("enter the number:"))
if num>=0:
    print(f"the number {num} is positive")
elif num<=0:
    print(f"the number {num} is negative")
else:
    print(f"the number is {num}")

#leap year checker
year=int(input("enter the year:"))
if year%400==0:
    print(f"year {year} is leap year")
else:
    print(f"year {year} is not a leap year")

#basic calculator
num1=int(input("Enter the number1:"))  
num2=int(input("Enter the number2:"))
operation=input("Enter cprresponding operation(+,-,*,/):") 
result=0
if operation=='+':
    result=num1+num2
    print("Result",result)
elif operation=='-':
    result=num1-num2
    print("Result",result)
elif operation=='*':
    result=num1*num2
    print("Result",result)
elif operation=='/':
    result=num1/num2
    print("Result",result)
else:
    print("Invalid operation")

#short hand if
num=int(input("enter the number to be checked")) 
result="the given number is even"if num%2==0 else "the given number is odd"  
print(result)

#discount calculator
product_cost=int(input("enter the product cost:"))
discount_for_product=int(input("enter the discount:")) 
result=product_cost*(discount_for_product/100) 
product_cost=result
print(f"product cost is{product_cost}")

#bmi calculator
weight=int(input("enter the weight in kg:"))
height=int(input("enter the height in m:"))
bmi=weight/(height)**2
print(f"the bmi of this person is{bmi}")
