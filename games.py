import random
from words import word_list
import string
from art import rps_pic, hangman_pic, treasure_pic
import peopledata

def guess_computers_num():
    """Number guessing game where the player guesses the computer's number."""
    print('\nYOU ARE GUESSING THE COMPUTERS NUMBER')
    
    while True:
        try:
            bound = int(input('What should my number be between? 1 - ? '))
            if bound > 1:
                break
            else:
                print('Please select an integer greater than 1')
        except ValueError:
            print('Please enter a valid number')
    
    num = random.randint(1, bound)
    guess = 0
    guesses = 0
    
    while guess != num:
        guess = int(input(f'Choose a number between 1 and {bound} '))
        if guess < num:
            print('nope, too low.')
        elif guess > num:
            print('nope, too high.')
        guesses += 1
    
    print(f'Congratulations! You guessed {num} correctly in {guesses} guesses!')

# guess the number you chooses
def guess_your_num():
    """Number guessing game where the computer guesses the player's number."""
    print('\nTHE COMPUTER WILL GUESS YOUR NUMBER')
    print('Think of a number and I\'ll try to guess it!')
    
    while True:
        try:
            bound = int(input('What range is your number in? 1 - ? '))
            if bound > 1:
                break
            else:
                print('Please select an integer greater than 1')
        except ValueError:
            print('Please enter a valid number')
    
    low = 1
    high = bound
    feedback = ''
    guesses = 0
    
    print(f'\nThink of a number between 1 and {bound}!')
    input('Press Enter when you\'re ready...')
    
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else: 
            guess = low
            
        guesses += 1
        feedback = input(f'\nIs your number {guess}? (H)igher, (L)ower, or (C)orrect? ').lower().strip()
        
        while feedback not in ['h', 'l', 'c']:
            feedback = input('Please enter H for higher, L for lower, or C for correct: ').lower().strip()
        
        if feedback == 'h':
            low = guess + 1
        elif feedback == 'l':
            high = guess - 1
    
    print(f'Yay! I guessed your number {guess} correctly in {guesses} guesses!')


def rock_paper_scissors():
    """Play a single round of rock paper scissors."""
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    
    user = input("\n'r' for rock, 'p' for paper, 's' for scissors: ").lower().strip()
    while user not in ['r', 'p', 's']:
        user = input("Please select a valid letter (r/p/s): ").lower().strip()
    
    comp = random.choice(['r', 'p', 's'])
    
    print(f"\nYou chose: {choices[user]}")
    print(f"Computer chose: {choices[comp]}")
    
    if comp == 'r':
        print(rps_pic[0])
    elif comp == 'p':
        print(rps_pic[1])
    else:
        print(rps_pic[2])
    
    if (user == 'r' and comp == 's') or (user == 'p' and comp == 'r') or (user == 's' and comp == 'p'):
        print('You won!')
        return 1
    elif (user == 'r' and comp == 'p') or (user == 'p' and comp == 's') or (user == 's' and comp == 'r'):
        print('You lost')
        return -1
    else:
        print('tie')
        return 0

def rps_best_of(rounds):
    """Play a best-of-X series of rock paper scissors."""
    print(f'YOU ARE PLAYING ROCK PAPER SCISSORS. BEST OF {rounds}')
    win = 0
    round = 1
    while round <= rounds:
        print(f'round {round}.')
        win += rock_paper_scissors()
        round += 1
        print(f'Score: You {(round-win)//2+max(win,0)} - {(round-win)//2+max(-win,0)} Computer')
    while win == 0:
        print('''\nITS A TIE!
                 \r play until someone wins''' )
        win += rock_paper_scissors()
    if win > 0:
        print('YOU WIN')
    elif win < 0:
        print('YOU LOSE')

def hangman():
    """Hangman word guessing game."""
    print('\nHANGMAN GAME')
    print('Guess the word one letter at a time!')
    
    word = random.choice(word_list).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    guessed = set()
    tries = 6
    while len(word_letters)>0 and tries > 0:
        letter_list = [l if l in guessed else '_' for l in word]
        
        print('\n' + hangman_pic[6-tries])
        print('Word: ' + ' '.join(letter_list))
        print(f'Letters used: {" ".join(sorted(guessed)) if guessed else "None"}')
        print(f'Remaining tries: {tries}')
        
        l = input('\nGuess a letter: ').upper().strip()
        if l in alphabet - guessed:
            guessed.add(l)
            if l in word_letters:
                word_letters.remove(l)
            else:
                tries -=1
        elif l in guessed:
            print(f'You have already guessed {l}. Try again.')
            continue
        elif l not in alphabet:
            print(f'please use a valid letter.')
            continue
        elif len(l) != 1:
            print('Please enter only one letter.')
            continue
    
    if tries == 0:
        print(f'Oh no, you ran out of tries, The word was {word}')
    else:
        print(f'''\n***************************************
                \rCongrats! You guessed {word} correctly!
                \r***************************************''')


# tic tac toe
def print_board(board):
    """Print the tic-tac-toe board."""
    print('\n   |   |   ')
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('___|___|___')
    print('   |   |   ')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('___|___|___')
    print('   |   |   ')
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print('   |   |   ')

def check_winner(board):
    """Check if there's a winner on the tic-tac-toe board."""
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]
    return None

def get_computer_move(board):
    """Get the computer's move using randomized AI."""
    # Always check if computer can win first (highest priority)
    win_moves = []
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_winner(board) == 'O':
                win_moves.append(i)
            board[i] = ' '
    if win_moves:
        return random.choice(win_moves)
    
    # Always check if computer needs to block player (second priority)
    block_moves = []
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_winner(board) == 'X':
                block_moves.append(i)
            board[i] = ' '
    if block_moves:
        return random.choice(block_moves)
    
    # Strategic moves with randomness
    available_moves = [i for i in range(9) if board[i] == ' ']
    
    # Sometimes take center (70% chance), sometimes be unpredictable
    if board[4] == ' ' and random.random() < 0.7:
        return 4
    
    # Take corners with randomization
    corners = [0, 2, 6, 8]
    available_corners = [corner for corner in corners if board[corner] == ' ']
    if available_corners and random.random() < 0.6:
        return random.choice(available_corners)
    
    # Take edges with some probability
    edges = [1, 3, 5, 7]
    available_edges = [edge for edge in edges if board[edge] == ' ']
    if available_edges and random.random() < 0.3:
        return random.choice(available_edges)
    
    # Take any available space (completely random)
    return random.choice(available_moves)

def tic_tac_toe():
    """Play tic-tac-toe against the computer."""
    print('\nTIC TAC TOE')
    print('You are X, computer is O')
    print('Positions are numbered 1-9:')
    print('\n 1 | 2 | 3 ')
    print('___|___|___')
    print(' 4 | 5 | 6 ')
    print('___|___|___')
    print(' 7 | 8 | 9 ')
    print('')
    
    board = [' '] * 9
    current_player = 'X'
    
    for turn in range(9):
        print_board(board)
        
        if current_player == 'X':
            while True:
                try:
                    move = int(input(f'\nEnter your move (1-9): ')) - 1
                    if 0 <= move <= 8 and board[move] == ' ':
                        board[move] = 'X'
                        break
                    else:
                        print('Invalid move! Choose an empty position (1-9).')
                except ValueError:
                    print('Please enter a number between 1 and 9.')
        else:
            move = get_computer_move(board)
            board[move] = 'O'
            print(f'Computer chooses position {move + 1}')
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == 'X':
                print('Congratulations! You won!')
            else:
                print('Computer wins! Better luck next time!')
            return
        
        current_player = 'O' if current_player == 'X' else 'X'
    
    print_board(board)
    print('It\'s a tie! Good game!')

# Band Name Generator
def band_name():
    """Generate a random band name based on user input."""
    place = input("your favourite city you lived in?  ")
    animal = input("what pet do you have/ want?  ")
    print(f'Your band name is {place}s {animal}s!')

# Love Calculator
def love_calculator():
    """Calculate love compatibility between two names."""
    print('WelcomE to the loOovEee CAalcuUlatOooOR')
    name1 = input('What is YOUR name?  ').lower()
    name2 = input ('What is THEIR name? ').lower()
    letters = name1 + name2
    true_points = 0
    for i in "true":
        true_points+=letters.count(i)
    love_points = 0
    for i in "love":
        love_points+=letters.count(i)
    points = int(str(true_points) + str(love_points))
    if points < 10 or points >90:
        print(f"Your score is {points}, you go together like coke and mentos.")
    elif points > 40 and points < 50:
        print(f"Your score is {points}, you are alright together." )
    else:
        print(f"Your score is {points}, maybe this isnt quite right.")


# Treasure hunt
def treasure_island():
    """Text-based adventure game to find treasure."""
    print(treasure_pic)
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    dead = False
    d1 = input("Which direction? Left (L) or Right (R)? ").upper()
    while d1 not in ["L", "R"]:
        d1 = input("Please choose a valid direction. Left (L) or Right (R)? ").upper()
    if d1 == "R":
        dead = True
        print("You have walked into a bears cave. Death by being eaten. GAME OVER")
    elif d1 == "L":
        d2 = input("You have arrived at the lake. What should you do next? Swim (S) or Walk (W)? ").upper()
        while d2 not in ["S", "W"]:
            d2 = input("Please choose a valid decision. Swim (S) or Walk (W)? ").upper()
        if d2 == "S":
            dead = True
            print("Oh no! Death by hypothermia. GAME OVER")
        elif d2 == "W":
            d3 = input("You have found 3 doors, a red door, a yellow door and a blue door./rChoose the one that might have the treasure (R), (Y), (B) ").upper() 
            while d3 not in ['R', 'B', 'Y']:
                d3 = input("Please select a valid door. (R), (Y), (B)")
            if d3 == "B":
                dead = True
                print("You found the room of blues :(. Death by sadness. GAME OVER")
            elif d3 == "Y":
                dead = True
                print("You found the room of lemons. Death by acidity. GAME OVER")
    if dead == False:
        print('CONGRATS YOU HAVE FOUND THE GOLD!')

# encrypt message
def encrypt(message, shift):
    """Encrypt a message using Caesar cipher."""
    alphabet = string.ascii_lowercase
    encrypted = ""
    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index + shift) % 26
            encrypted += alphabet[new_index]
        else:
            encrypted += letter
    return encrypted

# decrypt
def decrypt(message, shift):
    """Decrypt a message using Caesar cipher."""
    alphabet = string.ascii_lowercase
    decrypted = ""
    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index - shift) % 26
            decrypted += alphabet[new_index]
        else:
            decrypted += letter
    return decrypted

# Ceasar Cypher
def caesar_cipher():
    """Caesar cipher encryption and decryption game."""
    print('\nCAESAR CIPHER')
    print('Encrypt and decrypt secret messages!')
    
    while True:
        choice = input('\nType (E) to encrypt or (D) to decrypt: ').upper().strip()
        while choice not in ['E', 'D']:
            choice = input('Please select E or D: ').upper().strip()
        
        message = input('Enter your message: ').lower()
        
        while True:
            try:
                shift = int(input('Enter shift number (1-25): '))
                if 1 <= shift <= 25:
                    break
                else:
                    print('Please enter a number between 1 and 25')
            except ValueError:
                print('Please enter a valid number')
        
        if choice == 'E':    
            result = encrypt(message, shift)
            print(f'Encrypted message: {result}')
        else:
            result = decrypt(message, shift)
            print(f'Decrypted message: {result}')
        
        again = input('\nEncrypt/decrypt another message? (Y/N): ').upper().strip()
        while again not in ['Y', 'N']:
            again = input('Please enter Y or N: ').upper().strip()
        
        if again == 'N':
            break


# Black Jack
cards = ["ACE", 2, 3, 4, 5, 6, 7, 8, 9, 10, "JACK", "QUEEN", "KING"]
instructions = '''\nAn ACE can be 1 or 11.
                  \rJACK, QUEEN, KING have value 10.
                  \r The aim is to get the sum of your cards as close to 21.
                  \rIf the sum of your cards is higher than 21 BUST and you lose.'''

def value_bj(cards):
    """Calculate the value of a blackjack hand."""
    value = 0
    ace = False
    for i in range(len(cards)):
        if cards[i] in ["JACK", "QUEEN", "KING"]:
            value+=10
        elif cards[i] == 'ACE':
            value+=11
            ace = True
        else:
            value+=cards[i]
    if value > 21 and ace == True:
        value -= 10 
    if value > 21:
        return 0
    return value
        

def black_jack():
    """Play a game of blackjack against the computer."""
    print('\nYOU ARE PLAYING BLACK JACK')
    print(instructions)
    players_cards = []
    for _ in range(2):
        card = random.choice(cards)
        players_cards.append(card)
    comp_cards = []
    for _ in range(2):
        card = random.choice(cards)
        comp_cards.append(card)
    another = input(f'''\nYOUR CARDS: {players_cards}
                        \r COMPUTERS FIRST CARD: {comp_cards[0]}
                        \r Type 'Y' to get another card and 'N' to pass  ''').upper()
    if another == 'Y':
        pcard3 = random.choice(cards)
        players_cards.append(pcard3)
    if value_bj(comp_cards)<17:
        print('Computer is also choosing another card.')
        ccard3 = random.choice(cards)
        comp_cards.append(ccard3)
    players_score = value_bj(players_cards)
    comp_score = value_bj(comp_cards)
    print(f'''\nYOUR FINAL HAND: {players_cards} SCORE: {players_score}
              \rCOMPUTERS FINAL HAND: {comp_cards} SCORE: {comp_score}''')
    if players_score > comp_score:
        print('YOU WIN')
    elif players_score == comp_score:
        print('YOU TIE')
    else:
        print('YOU LOSE')


# Higher Lower
people = peopledata.data

def random_person():
    """Choose a random person from the celebrity data."""
    return random.choice(people)

def format_data(person):
    """Format celebrity data into printable format."""
    name = person["name"]
    description = person["description"]
    country = person["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(answer, person1, person2):
    """Check if the user's guess about follower counts is correct."""
    if person1['follower_count']>person2['follower_count']:
        return answer == 'A'
    else:
        return answer == 'B'

def higher_lower():
    """Guess which celebrity has more Instagram followers."""
    continue_game = True
    score = 0
    people_used=[]
    personA = random.choice(people)
    people_used.append(personA)
    personB = random.choice(people)
    while personB in people_used:
        personB = random.choice(people)
    people_used.append(personB)
    while continue_game == True:
        print(f"'\nCompare A: {format_data(personA)}.")
        print('\nvs')
        print(f"\nAgainst B: {format_data(personB)}.")
        guess = input("\nWho has more followers? Type 'A' or 'B': ").upper()
        is_correct = check_answer(guess, personA, personB)
        if is_correct == False:
            continue_game = False
            print(f"\nSorry, that's wrong. Final score: {score}")
        else:
            score+=1
            print(f"\nYou're right! Current score: {score}.")
            personA = personB
            personB = random.choice(people)
            while personB in people_used:
                personB = random.choice(people)
            people_used.append(personB)


def word_scramble():
    """Guess the word from its scrambled letters."""
    print('\nWORD SCRAMBLE')
    print('Unscramble the letters to guess the word!')
    
    word = random.choice(word_list).upper()
    scrambled_word = ''.join(random.sample(word, len(word)))
    
    # Make sure the scrambled word is different from the original
    while scrambled_word == word:
        scrambled_word = ''.join(random.sample(word, len(word)))
    
    attempts = 3
    print(f'\nScrambled word: {scrambled_word}')
    print(f'Hint: This is a {len(word)}-letter word')
    
    while attempts > 0:
        guess = input(f'\nYour guess (attempts left: {attempts}): ').upper().strip()
        
        if guess == word:
            print(f'Correct! The word was "{word}"!')
            print('Great job unscrambling!')
            return
        else:
            attempts -= 1
            if attempts > 0:
                print(f'Not quite right. Try again!')
                
                # Give a hint after first wrong guess
                if attempts == 2:
                    print(f'Hint: The word starts with "{word[0]}"')
                elif attempts == 1:
                    print(f'Hint: The word ends with "{word[-1]}"')
            else:
                print(f'Game over! The word was "{word}"')
                print('Better luck next time!')