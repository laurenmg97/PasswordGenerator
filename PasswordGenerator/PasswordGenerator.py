import random  

print('Welcome To Your Password Generator');

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmopqrstuvwxyz1234567890!@#$%^&*';

number = input('How many passwords should I generate? ');
number = int(number);

length = input("Length of password: ");
length = int(length);

print("\nHere are your passwords: ");

for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)


