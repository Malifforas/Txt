class Player:
    def __init__(self):
        self.name = ""
        self.gender = ""
        self.starter_pokemon = ""

    def select_gender(self):
        while self.gender != "M" and self.gender != "F":
            self.gender = input("Please select your gender (M/F): ").upper()

    def select_name(self):
        self.name = input("Please enter your name: ")

    def select_starter(self):
        starters = ["Chikorita", "Cyndaquil", "Totodile"]
        print("Welcome to the world of Pokemon Gold and Silver!")
        print("My name is Professor Elm.")
        print("This world is inhabited by creatures called Pokemon!")
        print("For some people, Pokemon are pets. Others use them for fights.")
        print("Myself... I study Pokemon as a profession.")
        print(f"{self.name}, I see that you're a new trainer.")
        print("First, what is your name?")
        self.select_name()
        print(f"Right! So your name is {self.name}!")
        print("Next, what is your gender?")
        self.select_gender()
        print(f"Alright, so you're a {self.gender}.")
        print("Now, let's choose your first Pokemon!")
        print("The three Pokemon available are:")
        for i in range(len(starters)):
            print(f"{i + 1}. {starters[i]}")
        while self.starter_pokemon not in starters:
            choice = input("Please select the number of the Pokemon you want: ")
            try:
                self.starter_pokemon = starters[int(choice) - 1]
                print(f"You have chosen {self.starter_pokemon} as your starter Pokemon!")
            except ValueError:
                print("Invalid selection. Please enter a number.")

    def start_journey(self):
        print(f"Congratulations on choosing {self.starter_pokemon} as your starter Pokemon!")
        print("Your journey as a Pokemon trainer is about to begin.")
        print("Professor Elm has given you a task to retrieve a rare Pokemon that was stolen from his lab.")
        print("The stolen Pokemon is one of the three starters: Chikorita, Cyndaquil, Totodile.")
        print(
            "You will have to travel around Johto region, catching new pokemons, battling trainers and gym leaders to improve your team and your skills.")
        print("You will be able to travel to Kanto region after defeating the Johto league.")
        print("But be warned, the thief is a skilled trainer and will not give up the Pokemon easily.")
        print("You will face many challenges and battles on your journey to retrieve the stolen Pokemon.")
        print("But with your trusty Pokemon by your side, you can overcome anything.")
        print("Good luck on your journey!")