import random
#import module

print("What is the max possible number you want to guess?")
max_number = ""
while not max_number.strip().isdigit():
    max_number = input("Enter a number:\n")
#ask for input
#if input is not integer, keep asking

random_number = random.randrange(int(max_number))
# generate a random number

guess = ""
counter = 0
while not str(random_number) == guess:
	guess = ""
	while not guess.isdigit():
		guess = input("Guess a number:\n")
		#check input is a integer or not
	counter +=1
	if random_number > int(guess):
		print("try a larger number")
	elif random_number < int(guess):
		print("try a smaller number")
	#check guessing is larger or smaller than the random number

print("Correct!\n You took",counter,"times to guess the correct number")