import random


all_guesses = [] 
secret_number = 0
attempts = 0

def game_start():
    """Game start + List khali kar do"""
    global secret_number, attempts, all_guesses
    secret_number = random.randint(1, 100)
    attempts = 0
    all_guesses = []  
    print("----- HIGH SCORE TRACKER -----")
    print("Maine 1-100 number socha. Sab guess save honge!")

def check_guess(guess):
    """Guess check + List mein daal do"""
    global attempts, all_guesses
    attempts += 1
    all_guesses.append(guess) 
    
    if guess < secret_number:
        print("Chota hai ⬆️")
        return False
    elif guess > secret_number:
        print("Bada hai ⬇️")
        return False
    else:
        print(f"SAHI! {secret_number} tha ")
        print(f"Total attempts: {attempts}")
        show_all_guesses() 
        return True

def show_all_guesses():
    """List ke sab item print karo"""
    print("\n----- TERE SAB GUESSES -----")
    print(f"Tune ye number try kiye: {all_guesses}")
    print(f"Sabse chota guess: {min(all_guesses)}") 
    print(f"Sabse bada guess: {max(all_guesses)}")   
    all_guesses.sort() 
    print(f"Sort karke: {all_guesses}")
    print("--------------------------------")

def get_user_input():
    """User se number lo - Safe wala"""
    while True:
        try:
            guess = int(input("Apna guess daal 1-100: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Bhai 1-100 ke beech")
        except ValueError:
            print("Number daal, text nahi")


def main():
    game_start()
    jeet_gaya = False
    
    while not jeet_gaya:
        user_guess = get_user_input()
        jeet_gaya = check_guess(user_guess)
    
    print("Game Over! ")


main()
