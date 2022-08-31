#Password generator
import random

# Input creating: how many type of char would you like to add to the password?
Big_letters_no = int(input("How many big letters do you do you wany in your password?"))
small_letters_no = int(input("How many small letters do you do you wany in your password?"))
number_no = int(input("How many numbers do you do you wany in your password?"))
symbols_no = int(input("How many symbols do you do you wany in your password?"))

#Creating a symbols, letters and numbers list

overall = [chr(element) for element in range(32,130)]

symbols = overall[:16] + overall[26:30] + overall[60:65]
random.shuffle(symbols)

Big_letters = overall[33:59]
random.shuffle(Big_letters)

Small_letters = overall[65:91]
random.shuffle(Small_letters)

numbers = overall[17:26]
random.shuffle(numbers)

#Single char type passwords creation

password_Big_letters = ''
i=0
while i < Big_letters_no:
    password_Big_letters += Big_letters[i]
    i += 1

password_small_letters = ''
j=0
while j < small_letters_no:
    password_small_letters += Small_letters[j]
    j += 1
    
password_numbers = ''
k=0
while k < Big_letters_no:
    password_numbers += numbers[k]
    k += 1
    
password_symbols = ''
h=0
while h < symbols_no:
    
    password_symbols += symbols[h]
    h += 1

#Combining small passwords into whole Password
    
Pre_password = password_Big_letters + password_small_letters + password_numbers + password_symbols
password_list = []
password_list += Pre_password
random.shuffle(password_list)

#Exchange the list to the string
Password = ''
for char in password_list:
    Password += char
    

print("Your password is: %s"%(Password))

