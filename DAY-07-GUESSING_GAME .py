import random


secret_number = 0
attempts = 0
max_number = 100



def game_start():
    """Game shuru karne ka function"""
    global secret_number, attempts  
    secret_number = random.randint(1, max_number)
    attempts = 0
    print(f"----- GUESS GAME 2.0 -----")
    print(f"Maine 1 se {max_number} ke beech number socha hai")

def check_guess(guess):
    """Guess check karne ka function - True/False return"""
    global attempts
    attempts = attempts + 1
    
    if guess < secret_number:
        print("Bahut chota hai ⬆️ Upar jaa")
        return False 
    elif guess > secret_number:
        print("Bahut bada hai ⬇️ Neeche aa")
        return False  
    else:
        print(f"SAHI PAKDE! Number {secret_number} tha ")
        print(f"Sirf {attempts} attempts mein")
        return True  

def get_user_input():
    """User se number lene ka function"""
    while True: 
        try:
            guess = int(input("Apna guess daal: "))
            if 1 <= guess <= max_number:
                return guess 
            else:
                print(f"Bhai 1 se {max_number} ke beech bol")
        except ValueError:
            print("Number daal bhai, text nahi")  
def play_again():
    """Firse khelne ka puchega"""
    choice = input("Fir khelna hai? haan/nahi: ").lower()
    if choice == "haan" or choice == "h":
        return True
    else:
        return False


def main():
    """Poora game control karta hai"""
    khelna_hai = True
    
    while khelna_hai:  
        game_start()  
        jeet_gaya = False
        
        while not jeet_gaya: 
            user_guess = get_user_input() 
            jeet_gaya = check_guess(user_guess)  
        
        khelna_hai = play_again() 
    


main() 
