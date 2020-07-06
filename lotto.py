# Saadiq Ryklief Class 1

from datetime import date
import sys

#This is to verify that the user is old enough to play
name = input('Please enter your name and surname: ')
current_year = date.today().year
year_of_birth = int(input('Enter year of birth: '))
age = current_year - year_of_birth
def get_users_age(age):
    """
    >>> age = int(18)
    >>> get_users_age(age)
    Testing
    True
    """
    if age >= 18:
        return True
    else:
        return False
get_users_age(18)

if age < 18:
    print('You are underage!')
    #[sys.exit()] is to stop the program from running if the user is underage
    sys.exit()
else:
    print('Welcome Ithuba National Lottery of South Africa')
import random

lotteryNumbers = []

#this code is for the program to generate 6 random numbers between 1 and 49
for i in range(0, 6):
    number = random.randint(1, 50)
    while number in lotteryNumbers:
        number = random.randint(1, 50)

    lotteryNumbers.append(number)

lotteryNumbers.sort()

# For the user to input their random numbers
lottoPlayerNum = []
for i in range(0, 6):
    try:
        number = int(input('Enter a number between 1 and 50: '))

        if number < 1 or number > 50:
            number = int(input("Number invalid, enter a number between 1 and 50: "))
        while number in lottoPlayerNum:
            number = int(input('number already in use, try again: '))
        while number in lotteryNumbers:
            number = random.randint(1, 50)
    except ValueError:
        number = int(input("only numbers accepted, try again: "))
    lottoPlayerNum.append(number)


lottoPlayerNum.sort()

# Displays the users numbers compared to programs numbers in a seperate file
file = open('result.txt', 'w')
sys.stdout = file
print('Hi ' + name + ', welcome Ithuba National Lottery of South Africa, you played on,', date.today())
print('Lottery Numbers: ')
print(lotteryNumbers)
print('Your Selection: ')
print(lottoPlayerNum)

counter = 0
for number in lottoPlayerNum:
    if number in lotteryNumbers:
        counter += 1

print("You have guessed " + str(counter) + " number(s) correctly")

# prints the users prize for how many numbers matched the programs numbers
counter = 0
for number in lottoPlayerNum:
    if number in lotteryNumbers:
        counter += 1

if counter == 6:
    print('YOU WON R10, 000 000.00')
if counter == 5:
    print('YOU WON R8,584.00')
if counter == 4:
    print('YOU WON R2,384.00')
if counter == 3:
    print('YOU WON R100.50')
if counter == 2:
    print('YOU WON R20.00')
if counter == 1:
    print('Sorry no prize, better luck next time!')
if counter == 0:
    print('Sorry no prize, better luck next time')
file.close()