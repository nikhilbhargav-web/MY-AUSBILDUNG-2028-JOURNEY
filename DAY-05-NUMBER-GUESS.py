import random

print("----- NUMBER GUESSING GAME -----")
print("main 1 se 100 tak ek number soch rha hu...")


secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("\nApna guess daal bhai: "))
    attempts = attempts + 1 
    
    if guess < secret_number:
        print("BHAI AUR BADA NUMBER SOCHO")
    elif guess > secret_number:
        print("BHAI THODA CHOTA NUMBER SOCHO")
    else:
        print(f"BOOM! SAHI PAKDA")
        print(f"SECRET NUMBER THA: {secret_number}")
        print(f"TUNE {attempts} ATTEMPTS MEIN JEET LIYA")
        break

    print("------ GAME OVER ------")
