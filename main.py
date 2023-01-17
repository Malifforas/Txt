from select_starter import SelectStarter
from Player import Player
# Create player
player = Player("Player1", [], None)

# Create an instance of SelectStarter
starter_selector = SelectStarter()

# Let player choose starter Pokemon
starter_selector.select()