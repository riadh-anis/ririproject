from curses.ascii import isalpha, isdigit


def try_me():

    age_guess = 0
    while (int(age_guess) != 32):
        age_input = input("For sake of simplicity, please enter an integer ya ? Guess Riadh's age:")
        # age_guess = age_input
        try:
            if int((age_input)) < 32:
                print( f'You have guessed Riadh is {age_input}')
                print("But he is a bit older than that")
            elif int((age_input)) > 32:
                print(f'You have guessed Riadh is {age_input}')
                print("He is a younger than that ! ")
                # age_guess = input("Try guessing Riadh's age again :")
            else :
                print("Congrats ! You guessed right! But who knows if it's true !")
            age_guess = age_input
        except ValueError:
            print("You do not listen, do you?")
