#sum of squaers
sum=0
for i in range(1,6):
    result = i**2
    sum += result
print(f"sum of 1 to 5 squares is {sum}")

#reverse printing 5 to 1
count = 5
while count>0:
    print(count)
    count -= 1

# multiplication table
num = int(input("enter the table wanted :"))
for i in range(1,11):
    print(f"{num} x {i} {num*i}")

#sum of all even
sum = 0
for i in range (11):
    if i%2 == 0:
       sum+= i
    print (sum)

#sum of all numbers from 1 to given
num = int(input("enter the number:"))
sum = 0
for i in range(num+1):
    sum+=i
print(sum)

# list displaying using ioop
num = [10,2,34,4,55,64,78,83,9]
for i in num:
    print(i)

#displaying -10 to -1
count += -10
while count <= 0:
    print(count)
    count+=1

#cube of all numbers
num = int(input("enter the number :"))
sun = 0
for i in range(1,num+1):
 sum=(i*i*i)
print(sum)

 