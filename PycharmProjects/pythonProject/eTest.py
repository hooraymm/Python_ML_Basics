import copy

list1 = [[10, 20], [30, 40], [50, 60]]

# shallow copy & deep copy
list2 = list(list1)
list3 = copy.deepcopy(list1)

list2[0]=[10,20]
print(id(list1[0])==id(list2[0]))
print(id(list1[2][1])==id(list3[2][1]))