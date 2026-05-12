# IGL AUSBILDUNG 2028 - DAY 7
# PROJECT: GUESSING GAME 2.0 WITH FUNCTIONS
# GOAL: while + def dono mix karna

import random

# ===== GLOBAL VARIABLES - Sab function use kar sakte =====
secret_number = 0
attempts = 0
max_number = 100

# ===== FUNCTIONS BANAYE - SAB KAAM ALAG DABBE MEIN =====

def game_start():
    """Game shuru karne ka function"""
    global secret_number, attempts  # Bahar wale variable use karne hain
    secret_number = random.randint(1, max_number)
    attempts = 0
    print(f"----- IGL GUESS GAME 2.0 -----")
    print(f"Maine 1 se {max_number} ke beech number socha hai")

def check_guess(guess):
    """Guess check karne ka function - True/False return"""
    global attempts
    attempts = attempts + 1
    
    if guess < secret_number:
        print("Bahut chota hai ⬆️ Upar jaa")
        return False  # Abhi nahi jeeta
    elif guess > secret_number:
        print("Bahut bada hai ⬇️ Neeche aa")
        return False  # Abhi nahi jeeta
    else:
        print(f"SAHI PAKDE! Number {secret_number} tha 🎉")
        print(f"Sirf {attempts} attempts mein")
        return True  # Jeet gaya!

def get_user_input():
    """User se number lene ka function"""
    while True:  # Jab tak sahi number na de
        try:
            guess = int(input("Apna guess daal: "))
            if 1 <= guess <= max_number:
                return guess  # Sahi number wapas bhej do
            else:
                print(f"Bhai 1 se {max_number} ke beech bol")
        except ValueError:
            print("Number daal bhai, text nahi")  # abc daala to error

def play_again():
    """Firse khelne ka puchega"""
    choice = input("Fir khelna hai? haan/nahi: ").lower()
    if choice == "haan" or choice == "h":
        return True
    else:
        return False

# ===== MAIN GAME LOOP - YAHAN SE GAME CHALTA =====
def main():
    """Poora game control karta hai"""
    khelna_hai = True
    
    while khelna_hai:  # Jab tak haan bolte raho
        game_start()  # Game reset karo
        jeet_gaya = False
        
        while not jeet_gaya:  # Jab tak na jeete
            user_guess = get_user_input()  # Number lo
            jeet_gaya = check_guess(user_guess)  # Check karo
        
        khelna_hai = play_again()  # Pooch: firse?
    

# ===== GAME START KARO =====
main()  # Ye line se poora game chalu hota