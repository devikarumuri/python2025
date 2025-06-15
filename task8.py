#reverselist using reverse
my_list=[10,20,30,40,50,11]
my_list.reverse()
print(my_list)
#reverselist using slicing
reversed_list=my_list[::-1]
print(reversed_list)

#commonelements
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
commonelements=[]
for item in list1:
    if item in list2:
        commonelements.append(item)
print(commonelements)
#unique elements
original_list=[1,2,2,3,4,4,5]
unique_list=[]
for numbers in original_list:
    if numbers not in unique_list:
        unique_list.append(numbers)
print(unique_list)

#remove duplication
duplicated_list=[1,2,2,3,4,4,5]
normal_list=[]
for numbers in duplicated_list:
    if numbers not in normal_list:
        normal_list.append(numbers)
print(normal_list)

#list concat
l1="hello"
l2="world"
print(l1+l2)

#list repeatation
l1="this is python which is object orientation/n"
repeat=l1*3
print(repeat)

#list removal
my_list=[10,20,30,40,50,60,70]
result=[my_list[i] for i in range(len(my_list))if i%2!=0]
print(result)

#list insertion
my_list=[1,2,3,4,5]
my_list2=[10,11,12]+my_list
print(my_list2)

#squares from 1 to 10
squares=[i**2 for i in range(1,11)]
print(squares)

#even numbers from 1 to 20
even_numbers=[i for i in range(1,21)if i%2==0]
print(even_numbers)

#len of words
words=["apple","banana","kiwi","grape"]
lengths=[len(word)for word in words]
length=[len(words)]
print(lengths)
print(length)