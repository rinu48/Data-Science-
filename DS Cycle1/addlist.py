List1 = [7, 5, 21, 18, 8]
List2 = [9, 15, 6, 3,11]

print ("list1 : " + str(List1))
print ("list2 : " + str(List2))
newList = []
for n in range(0, len(List1)):
 newList.append(List1[n] + List2[n])
print(newList)