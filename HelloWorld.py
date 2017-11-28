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



################################# FILE WORK ##################################
# f = open("ussyms.txt","r")
# st=time.clock()
# for line in f:
#     # print (line)
#     temp = line
# et=time.clock()
# print(et-st)


################################# ARRAY WORK ##################################
# st=time.clock()

# tempArray = []

# for i in range(0,1000000):
#     # print(i)
#     tempArray.append(i)
# et=time.clock()-st
# print (et)

# tempArray.sort(reverse=True)

# print(tempArray)


########################### DEFINING YOUR OWN FUNCTIONS #########################

# SAMPLES
# This function should return the string "Hello, World!"
def hello_world():
    return "Hello, World!"


# This function should return the parameter (x) times 3
def times_three(x):
    return x*3


# This function should return the parameter (x) cubed
def cube(x):
    return x*x*x


# YOUR TURN
# This function should return the parameter (x) squared

# def square(x):
#     return()

# def square(x):
#     return x*x

def square(x):
    y = x * x
    x = 5
    return y

toSquare = 5
result = square(toSquare)
print( "The result of " + str(toSquare) + " squared is " + str(result))



# This function should ask for your name, then return that string
# No test for this, try to test with a print statement
def your_name():
    # http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/io.html
    return 



# This function takes in a height and returns a half pyramid of that height,
# as an array of strings 
# EX: 
# half_pyramid(5)
# #
# ##
# ###
# ####
# #####
# Array looks like ["#", "##", "###", "####", "#####"]
def half_pyramid(x):    
    pyramid = []

    # Build your pyramid
    # for loop
        # print out the current row
        # print("something here")
        # append to array...
        # pyramid.append("something")

    return pyramid

def half_pyramid(n):
    for x in range(0, n):
        for y in range(0, x+1):
            print("*",end="")
        print("")
n = 5
half_pyramid(n)

def num_pyramid(n):
    number = 1
    for x in range(0, n):
        for y in range(0, x+1):
            print(number, end="")
        number = number + 1
        print("")
    
n = 5
num_pyramid(n)



# This function should take a symbol and, if the symbol exists in the s&p 
# stock symbol file, return the line number that the symbol exists on, 
# otherwise return 0
def find_symbol(sym):
    # open the file
    f = ""
    # start a counter
    count = 0

    # loop through the file, line by line
    for line in f:
        # add 1 to the counter
        count += 1
        # if the stock symbol is in the line, return the counter

    return 0