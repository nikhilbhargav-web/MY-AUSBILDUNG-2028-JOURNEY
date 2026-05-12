# IGL AUSBILDUNG 2028 - DAY 8
# PROJECT: HIGH SCORE TRACKER
# GOAL: List banana, append karna, loop se print karna

import random

# ===== GLOBAL LIST - Sab guesses yahan save honge =====
all_guesses = []  # Khali thaila shopping ke liye
secret_number = 0
attempts = 0

def game_start():
    """Game start + List khali kar do"""
    global secret_number, attempts, all_guesses
    secret_number = random.randint(1, 100)
    attempts = 0
    all_guesses = []  # Har naye game mein thaila khali
    print("----- IGL HIGH SCORE TRACKER -----")
    print("Maine 1-100 number socha. Sab guess save honge!")

def check_guess(guess):
    """Guess check + List mein daal do"""
    global attempts, all_guesses
    attempts += 1
    all_guesses.append(guess)  # Guess ko thaila mein daal diya
    
    if guess < secret_number:
        print("Chota hai ⬆️")
        return False
    elif guess > secret_number:
        print("Bada hai ⬇️")
        return False
    else:
        print(f"SAHI! {secret_number} tha 🎉")
        print(f"Total attempts: {attempts}")
        show_all_guesses()  # Sab guesses dikhao
        return True

def show_all_guesses():
    """List ke sab item print karo"""
    print("\n----- TERE SAB GUESSES -----")
    print(f"Tune ye number try kiye: {all_guesses}")
    print(f"Sabse chota guess: {min(all_guesses)}")  # List ka min
    print(f"Sabse bada guess: {max(all_guesses)}")   # List ka max
    all_guesses.sort()  # Chote se bada sort kar do
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

# ===== MAIN GAME =====
def main():
    game_start()
    jeet_gaya = False
    
    while not jeet_gaya:
        user_guess = get_user_input()
        jeet_gaya = check_guess(user_guess)
    
    print("Game Over! 💀")

# ===== GAME START =====
main()