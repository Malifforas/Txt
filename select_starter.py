class SelectStarter:
    def __init__(self):
        self.starter_pokemon = ""

    def select(self):
        starters = ["Chikorita", "Cyndaquil", "Totodile"]
        print("Welcome to the world of Pokemon Gold and Silver!")
        print("My name is Professor Elm.")
        print("This world is inhabited by creatures called Pokemon!")
        print("For some people, Pokemon are pets. Others use them for fights.")
        print("Myself... I study Pokemon as a profession.")
        print("First, what is your name?")
        self.name = input("Please enter your name: ")
        print(f"Right! So your name is {self.name}!")
        print("Now, let's choose your first Pokemon!")
        print("The three Pokemon available are:")
        for i in range(len(starters)):
            print(f"{i + 1}. {starters[i]}")
        while self.starter_pokemon not in starters:
            choice = input("Please select the number of the Pokemon you want: ")
            try:
                self.starter_pokemon = starters[int(choice) - 1]
                print(f"You have chosen {self.starter_pokemon} as your starter")
            except:
                print("Invalid input. Please select a number from 1 to 3.")