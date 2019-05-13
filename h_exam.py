# Exercise 1
# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
    # Extras:
        # Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
        # (Hint: order of operations exists in Python)
        # Print out that many copies of the previous message on separate lines. 
        # (Hint: the string "\n” is the same as pressing the ENTER button)


from datetime import datetime

name = input('What\'s your name? \n')
age = int(input('What\'s your age? \n'))
hundred = int((100-age) + datetime.now().year)
print ('Hello %s. You are %s years old. You will turn 100 years old in %s.' % (name, age, hundred))

repeat = int(input('Let\'s try again :   \n'))
sentence = ('Hello %s. You are %s years old. You will turn 100 years old in %s. \n' % (name, age, hundred))
print (sentence*repeat)



# Exercise 2 
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?
    # Extras:
        # If the number is a multiple of 4, print out a different message.
        # Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
        # If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = int(input("pick a number : "))
check = int(input("pick a number to it divide by: "))

if num % 4 == 0:
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)



# Exercise 3
# Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
    # Extras:
        # Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
        # Write this in one line of Python.
        # Ask the user for a number and return a list that contains only elements from the original list a that are smaller than 
        # that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print([i for i in a if i < 5])

new_list = []
for i in a:
    if i < 5:
        new_list.append(i)
        print(new_list)

num = int(input("Pick a number: "))
for i in a:
    if i < num:
        print(i)

# Exercise 4 
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = int(input("Pick a number : "))

RangeList = list(range(1,num+1))

DivisorList = []

for number in RangeList:
    if num % number == 0:
        DivisorList.append(number)

print(DivisorList)


# Exercise 5
# Take two lists, say for example these two:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.
    # Extras:
        # Randomly generate two lists to test this
        # Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random

one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 
two = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
both=[] 

if len(one) < len(two): 
    for i in one: 
        if i in two and i not in both: 
            both.append(i) 
if len(one) > len(two): 
    for i in two: 
        if i in one and i not in both: 
            both.append(i) 
print(both)

# je n'ai pas réussi la partie random :( 
# a = random.sample(range(1,30), 12)
# b = random.sample(range(1,30), 16)
# result = [i for i in a if i in b]


# Exercise 6
# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

word = input("Pick any word : ")

if word[::-1] == word[0:]:
    print(word, " is a palindrome")

else:
    print(word, " is not a palindrome")


# Exercise 7
# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
# Write one line of Python that takes this list a and makes a new list that has only the even 
# elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [i for i in a if i % 2 == 0]
print(b)


# Exercise 8
# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, 
# and ask if the players want to start a new game)
    # Remember the rules:
    # Rock beats scissors
    # Scissors beats paper
    # Paper beats rock

import sys

player1 = input("First player's name : ")
player2 = input("Second player's name : ")
player1_answer = input("%s, do yo want to choose rock, paper or scissors? " % player1)
player2_answer = input("%s, do you want to choose rock, paper or scissors? " % player2)

def compare(p1, p2):
    if p1 == p2:
        return("It's a tie!")
    elif p1 == 'rock':
        if p2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif p1 == 'scissors':
        if p2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif p1 == 'paper':
        if p2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(player1_answer, player2_answer))


# Exercise 9
# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercice)
    # Extras:
        # Keep the game going until the user types “exit”
        # Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

number = random.randrange(1, 10)
guess = 0
count = 0

while guess != number and guess != "exit":
    guess = input("Guess a number between 1 and 9. You can end the game by printing 'exit': ")

    if guess == "exit":
        print("Game Over")
        break

    guess = int(guess)
    count += 1
    if guess not in range(1, 10):
        print("You have to guess a number between 1 and 9!")
    elif guess < number:
        print("You've guessed too low!")
    elif guess > number:
        print("You've guessed too high!")
    else:
        if count == 1:
            print("You rock! You've got it at the first try!")
        elif count <= 3:
            print("Well done! You've got it in just {} tries".format(count))
        elif count > 3:
            print("You've got it! It took you {} tries!".format(count))

# Exercise 10
# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the 
# sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


#  F0 = 0, F1 = 1 et Fn = Fn – 1 + Fn – 2 pour n > 1


def fib (a, b):
    return a + b

num = int(input("How many Fibonacci numbers would you like to generate? "))

fib_list = []
for n in range(num):
    if n in [0, 1]:
        fib_list += [1]
    else:
        fib_list += [fib(fib_list[n-2], fib_list[n-1])]

print("The first", num, "Fibonacci numbers are:", fib_list)