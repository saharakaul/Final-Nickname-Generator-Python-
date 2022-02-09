#Nickname generator

#Import random library for random integers to generate random nickname
import random

#Ask User for First Name
First_Name = input("Please Enter your first name ")
#Ask User for Last Name
Last_Name = input("Please Enter your last name ")

#Nickname list
nickname_list = ["Cool", "Swag", "Nerd"]

#Main program loop
loop = True
while loop:
    #Display menu
    print("\nMain Menu")
    print("1.Change Name")
    print("2.Display a Random Nickname")
    print("3.Display All Nicknames")
    print("4.Add a nickname")
    print("5.Remove a nickname")
    print("6.Exit")

    #Get user command

    Number = int(input("What would you like to do? "))

    #Re-enter Name
    if Number == 1:
        #Ask User for First Name
        First_Name = input("Please Enter your first name ")
        # Ask User for Last Name
        Last_Name = input("Please Enter your last name ")

    #Print random nickname
    elif Number == 2:
        #Generate a random integer that falls within the legnth of the list
        x = random.randint(0, len(nickname_list)-1)
        #Print random nickname
        print(First_Name + " " + Last_Name + " " + nickname_list[x])

    #Print all nicknames
    elif Number == 3:
        #Loop until it has printed all list elements
        for element in nickname_list:
            #Print elements
            print(First_Name + " " + Last_Name + " " + element)
    #Add New Nickname
    elif Number == 4:
        #Allow user to input new nickname
        New_Nickname = input("Type in your new nickname ")
        #Add new nickname to the list
        nickname_list.append(New_Nickname)
    #Remove nickname
    elif Number == 5:
        #Get the nickname they want to get rid of
        Old_Nickname = input("Type in the nickname you would Like to Remove ")
        #Check if nickname is in the list
        if Old_Nickname in nickname_list:
            #Remove the nickname from the list
            nickname_list.remove(Old_Nickname)
        else:
            #Print error message
            print("Error, nickname not in list")
    #Exit
    elif Number == 6:
        #End while loop
        loop = False
        #Print exit message
        print("Exit")





