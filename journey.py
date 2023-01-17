from Player import Player
from select_starter import SelectStarter

player = Player("Player1", [], None)
starter_selector = SelectStarter()
starter_selector.select_starter(player)
def start_journey(self):
    # player has chosen their starter Pokemon
    print("Congratulations on choosing {} as your starter Pokemon!".format(self.starter_pokemon))
    print("Professor Elm gives you your Pokedex and sends you on your journey.")
    print("As you leave the lab, you run into a mysterious figure.")
    print("He introduces himself as Silver, a rival trainer.")
    print("He tells you that he's on a mission to collect powerful Pokemon.")
    print("You notice that he has a Pokemon with him that looks familiar.")
    print("He tells you that he just stole it from Professor Elm.")
    print("He challenges you to a battle to show off his new acquisition.")
    print("You accept the challenge and the battle begins...")
    # code for the battle goes here
