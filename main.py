import games
import random

def menu():
    game_choice = '0'
    menu_choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'B']
    while game_choice not in menu_choices:
        game_choice = input('''
                        PLEASE SELECT A NUMBER TO PLAY A GAME
                        1) Number Guessing Game - YOU GUESS
                        2) Number Guessing Game - YOU CHOOSE
                        3) Rock Paper Scissors
                        4) Hangman
                        5) Random Band Name Generator
                        6) Love Calculator
                        7) Find the Treasure
                        8) Ceasar Cipher
                        9) Black Jack
                        10) Higher or Lower - celebrities follower count
                        B) BACK
        
                            ''').upper()
    return game_choice

def get_to_game(choice):
    if choice != 'B': 
        if choice == '1':
            games.guess_computers_num()
        elif choice == '2':
            games.guess_your_num()
        
        elif choice == '3':
            rounds = int(input('How many rounds would you like to play?  '))
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
            games.ceasar_cypher()
        
        elif choice == '9':
            games.black_jack()
            
        elif choice == '10':
            games.higher_lower()

        again = input("\nTo play again type '1' otherwise select any button to return to the main menu")
        if again == '1':
            get_to_game(choice)
    return choice
     


def play():
    name = input('Hello, what is your name? ')
    choice = 1
    while choice != 'E':
        choice = input(f'\nHello {name}, would you like to see the game menu (M) or select a game randomly (R) or exit (E)?  ').upper()
        while choice not in ['M', 'R', 'E']:
            choice = input("\nPlease select 'M' for menu or 'R' for a randomly selected game or 'E' to exit ").upper()
        if choice == 'M':
            game_choice = menu()
            choice = get_to_game(game_choice)
        elif choice == 'R':
            random_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'])
            choice = get_to_game(random_choice)
    print('GOODBYE')


play()