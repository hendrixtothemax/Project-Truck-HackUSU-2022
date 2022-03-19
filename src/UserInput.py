
class UserInput:
    def __init__(self, prompt, numbOptions, optionsList):
        while True:
            # print out the prompt
            print(prompt)
            # Format and print options to the console
            options = ""
            for i in range(numbOptions):
                options += f"[{i+1}]: {optionsList[i]} "
            print(options)
            # Get User Input
            userInput = input("Your choice: ")
            # Parse User Input, If Input Valid, Return Integer, If Not, Reprompt User
            if userInput.isdigit():
                userInput = int(userInput)
                if userInput > 0 and userInput <= numbOptions:
                    return userInput

            print(f"Please input a choice between 1 and {numbOptions}")
