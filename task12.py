#set
#set intersection
set_1={1,2,3,4,5,6}
set_2={4,5,6,7,8,9}
set_3=set_1.intersection(set_2)
print(set_3)

#set union
set_1={1,2,3,4,5,6,7}
set_2={5,6,7,8,9,0}
set_3=set_1.union(set_2)
print(set_3)

#set difference
set_1={1,2,3,4,5,6,7} 
set_2={5,6,7,8,9,0}
set_3=set_1.difference(set_2)
print(set_3)

##set symmetric difference
set_1={1,2,3,4,5,6,7}
set_2={5,6,7,8,9,0}
set_3=set_1.symmetric_difference(set_2)
print(set_3)

#set membership test
my_set={1,2,3,4,5}
print(3 in my_set)