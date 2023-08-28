#Write a program to display the  number names of the digits of a number entered by user. 
digit=input("Enter a digit: ")
convo_list = list(digit)
convo_list_len=len(convo_list)
start= 0
store={
    0:"zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"
}
while start<convo_list_len:
    print(store[int(convo_list[start])], end = " ")
    
    start+=1
