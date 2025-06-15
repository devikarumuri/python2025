#exceptional handling
###########################################value error#################################################
num_1=int(input("enter the number 1:"))
num_2=int(input("enter the number 2:"))
print(num_1+num_2)
print(num_1-num_2)
print(num_1*num_2)
try:
    print(num_1/num_2)
except:
    print("error occured")
##########################################type error####################################################
x="5"
y=2
try:
    result=x+y
except TypeError as e:
    print(e)
#########################################file not found error###########################################
try:
    file=open("sample.txt","r")
    read=file.read()
    print(read)
except FileNotFoundError:
    print("The file was not found.")
##########################################finally block&else block:######################################
my_list=['k','l','m','v','b']
print(my_list[1])
try:
    print(my_list[10])
except Exception as e:
    print(e)
else:
    print(my_list[1])
finally:
    print("this is finally block used code")