#tuple #create a tuple
tuple_1=("devi","20yrs","white")
print(tuple_1)

#access tuple elements
week=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
print(week[4])

#tuple concat
tuple_1=(1,3,5)
tuple_2=(2,4,6)
tuple_3=tuple_1+tuple_2
print(tuple_3)

#tuple unpacking
length=float(input("Enter the length of the rectangle:"))
width=float(input("Enter the width of the rectangle:"))
area=length*width
print(f"the area of the above dimensions are {area}")

#element exist
tuple=(10,20,30,40,50)
element=30
if element in tuple:
    print(f"{element} exists in  the tuple.")
else:
    print(f"{element} does not exist in the tuple.")
#supermarket
items=[("Apple",99),("Banana",99),("Milk",49)]
total=0
print("Supermarket Bill")
print("-"*20)
for item,price in items:
    print(f"{item}:₹{price}")
    total+=price
print("-"*20)
print(f"Total:₹{total}")
