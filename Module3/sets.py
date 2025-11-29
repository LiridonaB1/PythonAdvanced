my_set = {1,2,3}
print(my_set)

set_ = set([4,5,6,6])
print(set_)

set1= {1,2,3}
set2= {3,4,5}

#UNION
union_result_method = set1.union(set2)
union_result_operator = set1 | set2

print('Union of set1 and set2 using union method:',union_result_method ) #12345
print('Union of set1 and set2 using union operator:',union_result_operator) #12345

#intersection

intersection_method = set1.intersection(set2)
intersection_operator = set1 & set2
print('Intersection of set1 and set2 using intersection method:',intersection_method ) #3
print('Intersection of set1 and set2 using intersection operator:',intersection_operator ) #3

#Difference
difference_method = set1.difference(set2) #1,2
difference_operator = set1 - set2
print('Difference of set1 and set2 using difference method:',difference_method )
print('Difference of set1 and set2 using difference operator:',difference_operator )



#Symetric_difference
symmetric_method = set1.symmetric_difference(set2)
symmetric_operator = set1 ^ set2
print('Symmetric difference of set1 and set2 using difference method:',symmetric_method ) #1,2,4,5
print('Symmetric difference of set1 and set2 using difference operator:',symmetric_operator ) #1,2,4,5



my_set= {1,2,3}
my_set.remove(3)
print(my_set)

my_set.add(5)
print(my_set)

my_set.discard(7)
print(my_set)





























