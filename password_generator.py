import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=[1,2,3,4,5,6,7,8,9,0]
symbols=['!','#','$','%','&','(',')','*','+']
print("Welcome to password generator")
nr_letter=int(input("How many letters would you like to have in your password\n"))
nr_symbols=int(input("Enter the number of symbols needed\n"))
nr_numbers=int(input("Enter the number of numbers in the password\n"))
#easy level
password=""
for char in range(1,nr_letter+1):
    password += str(random.choice(letters))
for char in range(1,nr_symbols+1):
    password +=str(random.choice(symbols))
for char in range(1,nr_numbers+1):
    password += str(random.choice(numbers))
    
print(password)


