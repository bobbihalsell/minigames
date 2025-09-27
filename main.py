import games
import random

def menu():
    """Display the main game menu and get user's choice."""
    game_choice = '0'
    menu_choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'B']
    while game_choice not in menu_choices:
        print("WELCOME TO THE MINI GAMES COLLECTION".center(60))
        game_choice = input('''
                        PLEASE SELECT A NUMBER TO PLAY A GAME
                        1) Number Guessing Game - YOU GUESS
                        2) Number Guessing Game - YOU CHOOSE
                        3) Rock Paper Scissors
                        4) Hangman
                        5) Random Band Name Generator
                        6) Love Calculator
                        7) Find the Treasure
                        8) Caesar Cipher
                        9) Black Jack
                        10) Higher or Lower - celebrities follower count
                        11) Tic Tac Toe
                        12) Word Scramble
                        B) BACK
        
                            ''').upper().strip()
        if game_choice not in menu_choices:
            print("Invalid choice! Please select a valid option.")
    return game_choice

def get_to_game(choice):
    """Route the user to the selected game."""
    if choice != 'B': 
        try:
            if choice == '1':
                games.guess_computers_num()
            elif choice == '2':
                games.guess_your_num()
            elif choice == '3':
                while True:
                    try:
                        rounds = int(input('How many rounds would you like to play? '))
                        if rounds > 0:
                            break
                        else:
                            print("Please enter a positive number.")
                    except ValueError:
                        print("Please enter a valid number.")
                games.rps_best_of(rounds)
            elif choice == '4':
                games.hangman()
            elif choice == '5':
                games.band_name()
            elif choice == '6':
                games.love_calculator()
            elif choice == '7':
                games.treasure_island()
            elif choice == '8':
                games.caesar_cipher()
            elif choice == '9':
                games.black_jack()
            elif choice == '10':
                games.higher_lower()
            elif choice == '11':
                games.tic_tac_toe()
            elif choice == '12':
                games.word_scramble()
        except KeyboardInterrupt:
            print("\n\nGame interrupted. Returning to menu...")
            return choice
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Returning to menu...")
            return choice

        again = input("\nTo play again type '1' otherwise press any key to return to the main menu: ").strip()
        if again == '1':
            get_to_game(choice)
    return choice
     


def play():
    print("      WELCOME TO THE MINI GAMES COLLECTION!")
    name = input('Hello, what is your name? ')
    choice = 1
    while choice != 'E':
        print(f"\nHello {name}! What would you like to do?")
        choice = input(f'''
(M) - Browse game menu
(R) - Play a random game  
(E) - Exit
        
Your choice: ''').upper().strip()
        
        while choice not in ['M', 'R', 'E']:
            choice = input("\nPlease select 'M' for menu, 'R' for random game, or 'E' to exit: ").upper().strip()
        
        if choice == 'M':
            game_choice = menu()
            choice = get_to_game(game_choice)
        elif choice == 'R':
            random_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
            print(f"Randomly selected game: {get_game_name(random_choice)}")
            choice = get_to_game(random_choice)
    
    print(f'\nGoodbye {name}! Thanks for playing!')


def get_game_name(choice):
    """Get the name of a game based on its choice number."""
    game_names = {
        '1': 'Number Guessing Game - YOU GUESS',
        '2': 'Number Guessing Game - YOU CHOOSE',
        '3': 'Rock Paper Scissors',
        '4': 'Hangman',
        '5': 'Random Band Name Generator',
        '6': 'Love Calculator',
        '7': 'Find the Treasure',
        '8': 'Caesar Cipher',
        '9': 'Black Jack',
        '10': 'Higher or Lower',
        '11': 'Tic Tac Toe',
        '12': 'Word Scramble'
    }
    return game_names.get(choice, 'Unknown Game')


if __name__ == "__main__":
    play()