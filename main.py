import random
# Random module will select a random number between 1 and 100

random_number = random.randint(1,100)
user_guess = -1
# This variable will count the number of guesses
guesses = 0
while(user_guess != random_number):
    guesses +=1
    user_guess = int(input("Guess a number:"))
    # If number is greater than the random number 
    if(user_guess > random_number):
        print("Lower number please")
    # If number is lower than the random number
    elif(user_guess< random_number):
        print("Higher number please")
    

print(f"You have guessed the number {random_number} in {guesses} guesses")