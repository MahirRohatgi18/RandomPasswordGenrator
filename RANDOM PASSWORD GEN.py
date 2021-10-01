import random # imports random module 
print("Do you want to Genrate a random password ? type Yes or No")
a = input("Enter Your Choice  :  ").capitalize()
#a = a.capitalize()
if a== 'Yes' :
    length = int(input("Enter the length of the password : "))
    print ("Genrating your Password")
    print ("Your Password is : ")
    # code for password
    pw= str() #empty string so it can be incremented later
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWQYZ1234567890!@#$%^&*()_=+-₹'
    #characters are defined
    for i in range (length): #goes through all possible permutations
        pw = pw + random.choice(characters) #adds a random choice to the string at every instance of i
    print(pw) # prints final pw
    
    # code for saving file :
    password = (pw)
    saveFile = open('RandomPassword.txt','x') # RandomPassword is file name 
    saveFile.write(str(password))
    saveFile.close() #file is saved where the main project is 
    
elif a=='No':
    print ("Have a nice day!")       
