#write a program to print all even numbers that falls between two numbers (exclusive both numbers) entered from the user using while loop in python

num_1 = int(input("Enter starting number: "))
num_2 = int(input("Enter end number: "))

while num_1<=num_2:
    if num_1%2 == 0:
       print(num_1)
    num_1+=1
    
