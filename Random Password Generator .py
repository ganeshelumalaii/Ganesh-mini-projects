import random
print("welcome to random password generator")
print("How do you want to make your passwords \n1.Easy 2.Medium 3.Strong")
choice=int(input("Enter your choice: "))
if choice == 1:
    random_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    no_of_passwords = int(input("Enter the number of passwords you want: "))
    i = 0
    while i<4:
        password_length = int(input("Enter the length of the passwords you want: "))
        i+=1
        if password_length<4:
            print("You must enter more than 8 characters")
        else:
            print("Here are your random passwords")
            for x in range(no_of_passwords):
                password=""
                for characters in range(password_length):
                    password = password + random.choice(random_characters)
                print(password)
            break

elif choice == 2:
    random_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    no_of_passwords = int(input("Enter the number of passwords you want: "))
    i = 0
    while i<4:
        password_length = int(input("Enter the length of the passwords you want: "))
        i+=1
        if password_length<4:
            print("You must enter more than 8 characters")
        else:
            print("Here are your random passwords")
            for x in range(no_of_passwords):
                password=""
                for characters in range(password_length):
                    password = password + random.choice(random_characters)
                print(password)
            break


elif choice == 3:
    random_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"
    no_of_passwords = int(input("Enter the number of passwords you want: "))
    i = 0
    while i<4:
        password_length = int(input("Enter the length of the passwords you want: "))
        i+=1
        if password_length<4:
            print("You must enter more than 8 characters")
        else:
            print("Here are your random passwords")
            for x in range(no_of_passwords):
                password=""
                for characters in range(password_length):
                    password = password + random.choice(random_characters)
                print(password)
            break
else:
    print("Invalid.Please Enter a Valid Number")

    
