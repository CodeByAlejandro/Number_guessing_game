#!/usr/bin/env python3

if __name__ == '__main__':
    import sys
    from random import randint

    # Check correct number of cmd line arguments
    num_of_args = len(sys.argv)
    if num_of_args != 3:
        print('Error: Please provide an integer lower and upper bound for ' +
              'this guessing game!', file=sys.stderr)
        sys.exit(1)

    # Check if boundaries are valid integers
    try:
        lower_bound = int(sys.argv[1])
        upper_bound = int(sys.argv[2])
    except ValueError:
        print('Error: Boundaries must be integers!', file=sys.stderr)
        sys.exit(1)

    # Calculate the game secret to guess
    secret_num = randint(lower_bound, upper_bound)

    # Main game loop
    wrongh_guess = True
    while wrongh_guess:
        # Initialize play round
        print('*' * 50)

        # Request guess
        guess = input(f"Please take a guess between {lower_bound} and " +
                      f"{upper_bound} 🙈\n(input 'q' or 'quit' to quit): ")

        # Allow the player to gracefully exit the game
        if guess.lower() in ('q', 'quit'):
            print('> Bye 👋\n')
            sys.exit(0)

        # Check if guess is an integer
        try:
            guess = int(guess)
        except ValueError:
            print('> You have to give me an integer number, dummy! 🤤\n')
            continue

        # Check if guess is in boundaries
        if guess < lower_bound or guess > upper_bound:
            print("> Now that's a pretty dumn guess ... 😏\n")
            continue

        # Check if guess is correct
        if guess == secret_num:
            print('> You found the secret number mate! 👌\n')
            wrongh_guess = False
        else:
            print("> I'm sorry, try again 😝\n")
            continue
