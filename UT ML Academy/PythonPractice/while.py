numList = [1,2,2,2,-2,-2]


sum = 0
index = 0
while (index < len(numList)):
    if (numList[index] >= 0):
        sum+= numList[index]
    index += 1

print(sum)

# 8.4

sumFor = 0
for num in numList:
    if num >= 0:
        sumFor += num
print(sumFor)






