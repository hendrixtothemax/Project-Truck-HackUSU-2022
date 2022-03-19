
class UserInput:
    def __init__(self, prompt, numbOptions, optionsList):
        self.prompt = prompt
        self.numbOptions = numbOptions
        self.optionsList = optionsList

    def getInput(self):
        while True:
            # print out the prompt
            print(self.prompt)
            # Format and print options to the console
            options = ""
            for i in range(self.numbOptions):
                options += f"[{i + 1}]{self.optionsList[i]} "
            print(options)
            # Get User Input
            userInput = input("Your choice: ")
            # Parse User Input, If Input Valid, Return Integer, If Not, Reprompt User
            if userInput.isdigit():
                userInput = int(userInput)
                if userInput > 0 and userInput <= self.numbOptions:
                    return userInput

            print(f"Please input a choice between 1 and {self.numbOptions}")
