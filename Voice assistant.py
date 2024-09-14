import datetime

# Function to take user input (simulates voice commands with text)
def take_command():
    return input("Type your command: ").lower()

# Function to greet the user
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        print("Good Morning!")
    elif 12 <= hour < 18:
        print("Good Afternoon!")
    else:
        print("Good Evening!")
    print("I am your assistant. How can I help you today?")

# Function for the assistant
def text_assistant(): 
    greet()
    while True:
        command = take_command()

        if 'time' in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {current_time}")

        elif 'stop' in command or 'exit' in command:
            print("Goodbye!")
            break

        else:
            print("Sorry, I can't do that yet.")

# Run the assistant
if __name__ == "__main__":
    text_assistant()
