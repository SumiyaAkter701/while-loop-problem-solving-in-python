# Write a programe to check whether a number is prime or not using while loop 
num = int (input("Type a number: "))
divided_by = 2
verifyprimenumber = 0
while divided_by< num:
    if num%divided_by==0:
        verifyprimenumber+=1
    divided_by+=1
if verifyprimenumber ==0:
    print("This is a Prime Number")
else:
    print("This is not a Prime Number")
