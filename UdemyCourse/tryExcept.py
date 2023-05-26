name = "Bob"

try:
    if name > 3:
        print("Your name is: " + name)
except:
    print("An error was detected")



name2 = "Anthony"

try:
    if len(name2) > 3:
        print(f"Your name has {len(name2)} letters")
except:
    print("An error was detected")