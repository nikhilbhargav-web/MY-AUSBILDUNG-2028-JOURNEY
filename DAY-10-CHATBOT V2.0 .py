import datetime 

chat_count = 0
user_name = ""

def igl_bot_v2(user_input):
    global chat_count
    user_input = user_input.lower()
    chat_count += 1 

    if user_input == "bye" or user_input == "exit":
        return "BREAK"

   
    elif user_input == "" or user_input == "skip":
        return "CONTINUE" 
    
    elif "stats" in user_input:
        return f"Tu ab tak {chat_count} message bhej chuka. Streak "

    
    elif "time" in user_input:
        now = datetime.datetime.now()
        return f"Abhi time hai: {now.strftime('%H:%M')} "

   
    elif "leipzig" in user_input:
        return "Leipzig 2028 Confirm 🇩🇪 SAP + AI + WFH "

    
    elif "day" in user_input:
        return "Tu Day 10 pe hai Nikhil Bhai 🟩 40 baaki"

    
    else:
        return "Samjha nahi. 'help' likh commands dekh "

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


def main():
    global user_name
    print("----- IGL CHATBOT v2.0 WHILE WALA -----")
    user_name = input("Bot: Tera naam kya hai bhai? ")
    print(f"Bot: Swagat {user_name}! 'help' likh commands ke liye")
    show_help()

    
    while True:
        user_ka_sawal = input(f"{user_name}: ")
        jawab = igl_bot_v2(user_ka_sawal)

       
        if jawab == "BREAK":
            print(f"Bot: Bye {user_name}! Cetaphil laga ke so ja ✨")
            print(f"Bot: Aaj {chat_count} baar baat hui. Kal Day 11 💀")
            break
          
        elif jawab == "CONTINUE":
            print("Bot: Khali message skip kar diya ⏭️")
            continue
        
        elif user_ka_sawal.lower() == "help":
            show_help()
            continue

       
        else:
            print("Bot:", jawab)


main()
