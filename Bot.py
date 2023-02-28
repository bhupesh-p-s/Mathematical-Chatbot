import re
import random

def greet():
    """Responds to user greetings."""
    # Define a list of possible user greetings
    greetings = ["hello", "hi", "hey"]
    # Define a list of possible bot greetings
    bot_greetings = ["Hello! How can I assist you today?", "Hi there! What can I help you with?", "Hey! How can I assist you?"]
    # Get user input and convert it to lowercase
    user_input = input("User: ").lower()
    # Check if user input is a greeting
    if user_input in greetings:
        # Select a random bot greeting and print it
        bot_greeting = bot_greetings[random.randint(0, len(bot_greetings)-1)]
        print("Bot:", bot_greeting)

def calculate():
    """Performs basic mathematical operations."""
    # Define a dictionary of possible mathematical operations and their symbols
    operations = {"addition": "+", "subtraction": "-", "multiplication": "*", "division": "/"}
    # Print a message asking the user what operation they want to perform
    print("Bot: What mathematical operation do you want to do? Choose from the following options:")
    # Print out all the possible operations for the user to choose from
    for key in operations.keys():
        print(key.capitalize())
    # Get user input for the desired operation and convert it to lowercase
    operation = input("User: ").lower()
    # Keep asking for an operation until the user selects a valid one
    while operation not in operations:
        print("Bot: That's not a valid operation. Please choose from the options above.")
        operation = input("User: ").lower()
    # Get user input for the two operands
    print("Bot: What is the first operand?")
    operand1 = float(input("User: "))
    print("Bot: What is the second operand?")
    operand2 = float(input("User: "))
    # If performing division, check that the second operand is not zero
    while operation == "division" and operand2 == 0:
        print("Bot: The second operand cannot be zero. Please enter a valid second operand.")
        operand2 = float(input("User: "))
    # Calculate the result of the operation
    result = eval(str(operand1) + operations[operation] + str(operand2))
    # Print out the result
    print("Bot: The " + operation + " of " + str(operand1) + " and " + str(operand2) + " is " + str(result))

if __name__ == "__main__":
    # Call the greet function to greet the user
    greet()
    # Call the calculate function to perform a mathematical operation
    calculate()
    # Keep asking the user if they want to perform another operation
    while True:
        print("Bot: Do you want to perform another operation? (Yes/No)")
        answer = input("User: ").lower()
        # If the user doesn't want to perform another operation, exit the loop and say goodbye
        if answer not in ["yes", "y"]:
            print("Bot: Thank you for using me. See you again.")
            break
        calculate()
