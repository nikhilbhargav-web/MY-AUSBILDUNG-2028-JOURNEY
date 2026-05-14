# IGL AUSBILDUNG 2028 - DAY 10
# PROJECT: IGL CHATBOT v2.0 
# GOAL: while loop + break + continue master karna

import datetime

# ===== GLOBAL DATA =====
chat_count = 0
user_name = ""

def igl_bot_v2(user_input):
    global chat_count
    user_input = user_input.lower()
    chat_count += 1 # Har message count

    # Command 1: Exit
    if user_input == "bye" or user_input == "exit":
        return "BREAK" # Special signal loop todne ka

    # Command 2: Skip
    elif user_input == "" or user_input == "skip":
        return "CONTINUE" # Khali message skip

    # Command 3: Stats
    elif "stats" in user_input:
        return f"Tu ab tak {chat_count} message bhej chuka. Streak 🔥"

    # Command 4: Time
    elif "time" in user_input:
        now = datetime.datetime.now()
        return f"Abhi time hai: {now.strftime('%H:%M')} ⏰"

    # Command 5: Leipzig
    elif "leipzig" in user_input:
        return "Leipzig 2028 Confirm 🇩🇪 SAP + AI + WFH 🏠"

    # Command 6: Day kitna
    elif "day" in user_input:
        return "Tu Day 10 pe hai Nikhil Bhai 🟩 40 baaki"

    # Default
    else:
        return "Samjha nahi. 'help' likh commands dekh 😅"

def show_help():
    """Menu dikhao"""
    print("\n----- IGL BOT COMMANDS -----")
    print("leipzig  - Leipzig plan")
    print("time     - Current time")
    print("stats    - Kitne message bheje")
    print("day      - Konsa day chal raha")
    print("skip     - Khali message bhej")
    print("bye      - Bot band karo")
    print("----------------------------\n")

# ===== MAIN PROGRAM =====
def main():
    global user_name
    print("----- IGL CHATBOT v2.0 WHILE WALA -----")
    user_name = input("Bot: Tera naam kya hai bhai? ")
    print(f"Bot: Swagat {user_name}! 'help' likh commands ke liye")
    show_help()

    # WHILE LOOP START - Jab tak True hai chalta rahega
    while True:
        user_ka_sawal = input(f"{user_name}: ")
        jawab = igl_bot_v2(user_ka_sawal)

        # BREAK CONDITION
        if jawab == "BREAK":
            print(f"Bot: Bye {user_name}! Cetaphil laga ke so ja ✨")
            print(f"Bot: Aaj {chat_count} baar baat hui. Kal Day 11 💀")
            break # Loop yahi khatam

        # CONTINUE CONDITION  
        elif jawab == "CONTINUE":
            print("Bot: Khali message skip kar diya ⏭️")
            continue # Is baar reply nahi, wapas input pe jao

        # HELP CONDITION
        elif user_ka_sawal.lower() == "help":
            show_help()
            continue

        # NORMAL REPLY
        else:
            print("Bot:", jawab)

# ===== PROGRAM START =====
main()
