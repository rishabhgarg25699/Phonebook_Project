print("")
print("****************PHONEBOOK******************")
print("*******STORE YOUR NAMES AND CONTACTS*******")
print("")
print("*******MENU DRIVEN PROGRAM*************")
print("1. Do you want to enter the entry")
print("2. Search the phone number by name")
print("3. Delete an entry")
print("4. Display the phonebook")
print("5. EXIT for the phonebook\n")

while(1):

    print("\n")
    option = int(input("Type your another option  "))

    if option == 1:
        n = int(input("How many names do you want to store  "))
        print(" ")
        print("Please enter the name and their numbers  ")
        print("  ")
        dictionary = {}
        i = 0
        for i in range(n):
            name, *line = input().split()
            scores = list(map(int, line))
            dictionary[name] = scores

    elif option == 4:
        print(dictionary)

    elif option == 3:
        delete = input("Enter the element to be deleted  ")
        del dictionary[delete]

    elif option == 5:
        exit()

    else:
        name = input("Enter the name to be searched  ")
        print(dictionary.get('name'))
