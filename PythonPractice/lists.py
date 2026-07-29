# # list1 = [1, 4, 9, 5]
# list2 = ["red", "green", "blue"]
# list3 = [2, "hello", 3.5, 8]

# print(list3[2])
# print(list1[0])
# print(list2[-1])

# #5.1b r and l

# myfirstlist = [0,0,0,0,0,0]

# def changeList(list1, index, string):
#     list1[index] = string
#     return list1

# print(changeList(myfirstlist, 2, "uwu"))

lst = [ [1,2,3], 

 [4,5,6], 

 [7,8,9] ]

print(lst[2][1])
print("")

hotel = [ ["available", "available", "available", "Angie", "Brian"], 
["Claire", "available", "available", "available", "available", "available"],
["available", "available", "David", "available", "available"],
["available", "Emily", "available", "available", "available"]]

print(hotel[3][1])
print(hotel[1][4])

hotel[2][3] = "Frank"

print(hotel)
