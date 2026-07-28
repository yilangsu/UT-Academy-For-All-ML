
# for i in range(5):
#    print(i)

# def forprint(start, end):
#     if start > end:
#         print("range error")
#     else:
#         for i in range (start, end):
#             print(i)

# forprint(3,35)

# myList = [1,2,3,4,5,5,5,5,5]

# def doubleList(numList):
#     for i in range(len(numList)):
#         numList[i] = numList[i]*2
#     return numList

# print(doubleList(myList))

list1 = ["red", "blue", "green"]

def color(list1):
    for i in range(len(list1)):
        print(i, list1[i])

color(list1)