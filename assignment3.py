import random

play_again = "y"

# Keep playing as long as the user enters "y"
while play_again == "y":

    # Computer chooses a random number between 1 and 100
    random_number = random.randint(1, 100)
    guesses = 0

    # Keep asking for guesses until the user guesses correctly
    while True:

        # Ask the user for a guess
        guess = int(input("Enter a guess between 1 and 100: "))

        # Make sure the guess is between 1 and 100
        while guess < 1 or guess > 100:
            print("Invalid guess. Please try again")
            guess = int(input("Enter a guess between 1 and 100: "))

        # Count the valid guess
        guesses += 1

        # Compare the guess to the random number
        if guess > random_number:
            print("Lower")
        elif guess < random_number:
            print("Higher")
        else:
            print("Congratulations!")
            print(f"Number of guesses: {guesses}")

            # Give the player feedback based on their number of guesses
            if guesses <= 3:
                print("You are amazing")
            elif guesses <= 5:
                print("Impressive")
            elif guesses <= 7:
                print("Good job!")
            elif guesses <= 9:
                print("Took a little longer, but you got there")
            else:
                print("You need to lock in")

            break

    # Ask if the user wants to play again
    play_again = input("Press y if you want to play again: ").lower()