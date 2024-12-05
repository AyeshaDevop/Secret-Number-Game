import random

def main():
    """
    A number guessing game where the user attempts to guess a randomly chosen number.
    """
    secret_number = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99...")

    while True:
        try:
            guess = int(input("Enter a guess: ")) 
            if guess < 0 or guess > 99:
                print("Please enter a number between 0 and 99.")
                continue
            
            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print(f"Congrats! The number was: {secret_number}")
                break  
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == '__main__':
    main()
