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
st=time.clock()
for i in range(0,1000000):
    # print(i)
    temp = i
et=time.clock()-st
print (et)