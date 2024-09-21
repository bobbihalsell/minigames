import random
from words import word_list
import string
from art import rps_pic, hangman_pic, treasure_pic
import peopledata

# guess the number computer chooses
def guess_computers_num():
    print('YOU ARE GUESSING THE COMPUTERS NUMBER')
    bound = int(input('What should my number be between? 1 - ?  '))
    valid_bound = isinstance(bound, int) and bound>1
    while valid_bound==False:
        bound = int(input('''
        \nPLEASE SELECT AN INTEGER GREATER THAN 1
        \rWhat should my number be between? 1 - ?  '''))
        valid_bound = isinstance(bound, int) and bound>1
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
    print(f'Congrats! you have guessed {num} correctly in {guesses} guesses!')


# guess the number you chooses
def guess_your_num():
    print('THE COMPUTER WILL GUESS YOUR NUMBER. CHOOSE A NUMBER.')
    bound = int(input('What is your number between? 1 - ?  '))
    valid_bound = isinstance(bound, int) and bound>1
    while valid_bound==False:
        bound = int(input('''
        \nPLEASE SELECT AN INTEGER GREATER THAN 1
        \rWhat is your number between? 1 - ?  '''))
        valid_bound = isinstance(bound, int) and bound>1
    low = 1
    high = bound
    feedback = ' '
    guesses = 0
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else: 
            guess = low
        feedback = input(f'''\n Is {guess} too high (H) too low (L) or correct (C)? ''').lower()
        if feedback == 'h':
            high = guess - 1
            guesses += 1
        elif feedback == 'l':
            low = guess + 1
            guesses += 1
    print(f'Yay, computer guessed your number, {guess}, correctly in {guesses} guesses!')


def rock_paper_scissors():
    user = input("'r' for rock, 'p' for paper, 's' for scissors  ").lower()
    while user not in ['r', 'p', 's']:
        user = input('''
        \n Please select a valid letter.
        \r 'r' for rock, 'p' for paper, 's' for scissors  ''')
    comp = random.choice(['r', 'p', 's'])
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

def rps_best_of(x):
    print(f'YOU ARE PLAYING ROCK PAPER SCISSORS. BEST OF {x}')
    win = 0
    round = 1
    while round <= x:
        win += rock_paper_scissors()
        round += 1
    while win == 0:
        print('''\nITS A TIE!
                 \r play until someone wins''' )
        win += rock_paper_scissors()
    if win > 0:
        print('YOU WIN')
    elif win < 0:
        print('YOU LOSE')

def hangman():
    print('YOU ARE PLAYING HANGMAN')
    word = random.choice(word_list).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    guessed = set()
    tries = 6
    while len(word_letters)>0:
        letter_list = [l if l in guessed else '-' for l in word]
        print(hangman_pic[6-tries])
        print(' '.join(letter_list))
        print('Letters used: ', ' '.join(guessed))
        l = input(f'You have {tries} tries remaining. Guess a letter: ').upper()
        if l in alphabet - guessed:
            guessed.add(l)
            if l in word_letters:
                word_letters.remove(l)
            else:
                tries -=1
        elif l in guessed:
            print(f'You have already guessed {l}. Try again.')
        elif l not in alphabet:
            print(f'please use a valid letter.')
        if tries == 0:
            print(f'Oh no, you ran out of tries, The word was {word}')
            break
    if len(word_letters)==0: 
        print(f'''\n***************************************
                \rCongrats! You guessed {word} correctly!
                \r***************************************''')


# tic tac toe


        



# Band name generator
def band_name():
    place = input("your favourite city you lived in?  ")
    animal = input("what pet do you have/ want?  ")
    print(f'Your band name is {place}s {animal}s!')

# Love Calculator
def love_calculator():
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
    alphabet_string = string.ascii_lowercase
    alphabet = list(alphabet_string)
    enc_mess = ""
    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index= (index + shift) % 26
            enc_mess += alphabet[new_index]
        else:
            enc_mess += letter
    return enc_mess

# decrypt
def decrypt(message, shift):
    alphabet_string = string.ascii_lowercase
    alphabet = list(alphabet_string)
    dec_mess = ""
    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index= (index - shift) % 26
            if new_index < 0:
                new_index+= 26
            dec_mess += alphabet[new_index]
        else:
            dec_mess += letter
    return dec_mess

# Ceasar Cypher
def ceasar_cypher():
    again =0
    while again !='N':
        choice = input('Type (E) to encrypt your message and (D) to decrypt your message ').upper().strip()
        while choice not in ['E', 'D']:
            choice = input('Please select a valid option, (E), (D).').upper().strip()
        message = input('Type your message:\n').lower()
        shift = int(input('Type the shift number\n'))
        if choice == 'E':    
            enc = encrypt(message, shift)
            print(f'Your encrypted message is:\n{enc}')
        if choice == 'D':
            dec = decrypt(message, shift)
            print(f'Your decrypted message is:\n{dec}')
        again = input('Would you like to encrypt or decrypt again (Y/N)?\n').upper()
        while again not in ['Y', 'N']:
            again = input('Please select Y or N?\n').upper()


# Black Jack
cards = ["ACE", 2, 3, 4, 5, 6, 7, 8, 9, 10, "JACK", "QUEEN", "KING"]
instructions = '''\nAn ACE can be 1 or 11.
                  \rJACK, QUEEN, KING have value 10.
                  \r The aim is to get the sum of your cards as close to 21.
                  \rIf the sum of your cards is higher than 21 BUST and you lose.'''

def value_bj(cards):
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
    """chooses a random person"""
    return random.choice(people)

def format_data(person):
    """Format account into printable format: name, description and country"""
    name = person["name"]
    description = person["description"]
    country = person["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(answer, person1, person2):
    if person1['follower_count']>person2['follower_count']:
        return answer == 'A'
    else:
        return answer == 'B'

def higher_lower():
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