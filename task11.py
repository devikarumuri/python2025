#dictionary update
my_dict={'name':'python','age':'25'}
dict={'city':'hyderabad'}
my_dict.update(dict)
print(my_dict)

#dictionary access
product_info={'name':'laptop','brand':'dell','price':30000,'series':'gaming'}
print(product_info.get('price'))

#dictionary removal
my_info={'name':'karthik','age':'20','qualification':'b.tech','place':'hyderabad'}
my_info.pop('place')
print(my_info)

#printing only dictionary keys
my_key={'name':'meena','age':26,'place':'bhimavaram','qualification':'hr'}
print(my_key.keys())

#printing only dictionary values
my_value={'name':'meena','age':26,'place':'bhimavaram','qualification':'hr'}
print(my_value.values())

#dictionary through input
dictionary={}
student_id=int(input("enter the student_id:"))
student_name=input("enter the student name:")
dictionary[student_id]=student_name
print(dictionary)



