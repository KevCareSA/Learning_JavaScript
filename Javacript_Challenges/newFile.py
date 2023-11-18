# Import necessary libraries
import random
import datetime

# Define the AI assistant's name
name = "AI Assistant"

# Define a function to greet the user
def greet():
    # Get the current time
    current_time = datetime.datetime.now().time()

    # Define a list of possible greetings
    greetings = ["Good morning", "Good afternoon", "Good evening"]

    # Choose a random greeting from the list
    greeting = random.choice(greetings)

    # Print the greeting and the current time
    print(f"{greeting}, I am {name}. The time is {current_time}.")

# Call the greet function to start the conversation
greet()

# Define a function to handle user input
def handle_input():
    # Get user input
    user_input = input("How can I assist you? ")

    # Print the user input
    print(f"You said: {user_input}")

# Call the handle_input function to handle user input
handle_input()
