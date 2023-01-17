class Player:
    def __init__(self, name, party=None, location=None):
        self.name = name
        self.party = [] if party is None else party
        self.location = location
        self.items = []

    def move(self, destination):
        if self.location is None:
            print("Error: Player's current location is not set.")
            return
        if destination not in self.location.routes:
            print("Error: Destination is not reachable from the current location.")
            return
        self.location = destination
        print("You have arrived at", destination.name)

    def check_money(self):
        try:
            print(self.money)
        except AttributeError:
            print("Error: Player does not have any money.")