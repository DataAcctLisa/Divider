#To create a list of numbers from 2 to 10, just use the following code:

x=range(2,1000)
#print(list(x))

#for elem in x:
#    print(elem)

# Create a program that asks the user for a number 
# and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number 
# that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = (int(input("choose a number: ")))
x = list(range(1, num + 1))
print([ i for i in x if num %i == 0 ])


#the above code works great for finding the greatest common factor





