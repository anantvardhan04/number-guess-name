import random


# Function definitions
def get_difficulty():
    while True:
        try:
            difficulty = int(input("Enter your choice: "))
            if difficulty in [1, 2, 3]:
                return difficulty
            else:
                print("Invalid choice. Please select a valid choice among [1,2,3].")
        except ValueError:
            print("Invalid Input. Please enter an integer.")


def get_guess():
    while True:
        try:
            user_input = int(input("Enter your guess: "))
            return user_input
        except ValueError:
            print("Invalid Input. Please enter an integer.")
            continue


def main():
    random_number = random.randint(1, 100)
    number_of_attempts = 0

    print(
        """Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.\n
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)\n"""
    )

    difficulty = get_difficulty()

    if difficulty == 1:
        print("Great! You have selected the Easy difficulty level.")
        number_of_chances = 10
    elif difficulty == 2:
        print("Great! You have selected the Medium difficulty level.")
        number_of_chances = 5
    elif difficulty == 3:
        print("Great! You have selected the Hard difficulty level.")
        number_of_chances = 3

    print("Let's start the game!\n")

    while number_of_chances > 0:
        number_of_attempts += 1
        user_input = get_guess()
        if user_input == random_number:
            print(
                f"Congratulations! You guessed the correct number in {number_of_attempts} attempts."
            )
            break
        else:
            if random_number < user_input:
                print(f"Incorrect! The number is less than {user_input}")
            else:
                print(f"Incorrect! The number is greater than {user_input}")
            number_of_chances -= 1

        if number_of_chances == 0:
            print(f"Game Over! The correct number was {random_number}.")


if __name__ == "__main__":
    main()
