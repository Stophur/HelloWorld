import os
import time
# a = os.getcwd()
# x="13 "
# y="BROKE"
# c = "HEY CHRIS, SORRY I BROKE YOUR STUFF"

# print(x,y, c)

# print ("test")

# x = "10"
# y = "10"

# x=y
# print(x+y)
# print(int(x)+int(y))

# start = 1
# temp = 1
# st=time.clock()
# for i in range(0,1000000):
#     # print(i)
#     temp = i
# et=time.clock()-st
# print (et)


# FILE WORK
f = open("ussyms.txt","r")
st=time.clock()
for line in f:
    # print (line)
    temp = line
et=time.clock()
print(et-st)


# ARRAY WORK
st=time.clock()

tempArray = []

for i in range(0,1000000):
    # print(i)
    tempArray.append(i)
et=time.clock()-st
print (et)

tempArray.sort(reverse=True)

print(tempArray)