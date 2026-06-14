print("Welcome to ChatBot")
while True:
    command=input("Enter your text (or \"Exit\" to finish):- ").upper()
    if command == "EXIT":
        break
    if command == "HI":
        print("Hello! How are you?")
    elif command == "HELLO":
        print("Hi there!")
    elif command == "HOW ARE YOU":
        print("I'm doing great. Thanks for asking!")
    elif command == "WHAT IS YOUR NAME":
        print("My name is CodeAlpha Bot.")
    elif command == "WHO CREATED YOU":
        print("I was created using Python.")
    elif command == "GOOD MORNING":
        print("Good morning! Have a great day.")
    elif command == "GOOD EVENING":
        print("Good evening! Hope you're doing well.")
    elif command == "THANK YOU":
        print("You're welcome!")
    elif command == "BYE":
        print(" Goodbye! Have a nice day.")
        break
    elif command == "SEE YOU LATER":
        print(" See you soon.")
    elif command == "HELP":
        print("I can respond to basic greetings and questions.")
    elif command == "WHAT CAN YOU DO":
        print("I can have simple conversations with you.")
    else:
        print("Sorry, I don't understand that.\nI have the following of questions you can ask and I can reply :-\n hi\n hello\n how are you\n what is your name\n who created you\n good morning\n good evening\n thank you\n bye\n see you later\n help\n what can you do")