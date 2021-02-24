import random


def get_movie_name():
    # getting a movie name to play

    movies = ['titanic', 'avatar', 'matrix', 'inception', 'interstellar', 'predestination', 'batman',
              'superman', 'spiderman', 'transformers']
    return random.choice(movies)


def get_user_name():
    # getting user's name

    name = input("What is your name? ")
    print(f"Good luck! {name}")


def hangman():
    # working of the game

    get_user_name()
    print("\nGuess the movie name")
    movie = get_movie_name()
    movie_letters = set(movie)  # unique letters of movie
    used_letters = set()  # letters guessed by user
    guess = ["_" for i in range(len(movie))]  # movie name in blanks
    lives = 5

    while ''.join(guess) != movie and lives > 0:
        # when not guesssed and atleast 1 life left

        print(
            f"You have {lives} lives left and used ({','.join(used_letters)}) letters.\n")
        print(' '.join(guess))
        letter = input("Guess a letter: ")

        if letter not in used_letters:
            used_letters.add(letter)  # adding used letter

            if letter in movie_letters:  # adding letters to guess variable
                for i in range(len(guess)):
                    if movie[i] == letter:
                        guess[i] = letter

        elif letter in used_letters:  # minus 1 life if wrong
            print(f"You have already used {letter}.")
            lives -= 1

    # gets here if out of lives or guessed correctly
    if lives == 0:
        print(f"\nYou Lost! Goodluck next time.\nThe movie is {movie}.")
    else:
        print(f"\n{movie}\nYou Won! Congratulations!\nYou guessed it correctly")


hangman()
