# Assignment_number_1
# Question_number_1 = write a python program to get the fibonacci series between 0 to 50

number  = int(input("enter the number to get fibonacci sereis : "))
first_number = 0
second_number = 1
for i in range (8):
    third_number = first_number + second_number
    first_number = second_number
    second_number = third_number
    print (third_number , end = "  ")

