import random
class Battle:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent
        self.player_pokemon = player.party[0]
        self.opponent_pokemon = opponent.party[0]
        self.is_running = True

    def start(self):
        print(f"A wild {self.opponent_pokemon.name} appeared!")
        while self.is_running:
            print("What would you like to do?")
            print("1. Attack")
            print("2. Switch Pokemon")
            print("3. Use Item")
            print("4. Run")
            choice = input("Enter the number of your choice: ")
            if choice == "1":
                self.player_attack()
            elif choice == "2":
                self.player_switch()
            elif choice == "3":
                self.player_use_item()
            elif choice == "4":
                self.player_run()
            else:
                print("Invalid choice. Please enter a number from 1 to 4.")
            if self.opponent_pokemon.is_fainted():
                print(f"{self.opponent_pokemon.name} fainted!")
                self.is_running = False
                continue
            self.opponent_attack()
            if self.player_pokemon.is_fainted():
                print(f"{self.player_pokemon.name} fainted!")
                self.is_running = False

    def player_attack(self, player_pokemon, opponent_pokemon):
        # Display player's Pokemon's moves and ask player to select one
        print("{}'s moves:".format(player_pokemon.name))
        for i in range(len(player_pokemon.moves)):
            print("{}. {} (PP: {})".format(i + 1, player_pokemon.moves[i].name, player_pokemon.moves[i].pp))
        while True:
            try:
                move_choice = int(input("Select a move: "))
                if move_choice < 1 or move_choice > len(player_pokemon.moves):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please select a move by its number.")

        selected_move = player_pokemon.moves[move_choice - 1]

        if selected_move.pp <= 0:
            print("{} has no PP left for {}.".format(player_pokemon.name, selected_move.name))
            return

        # Check for move accuracy
        if random.randint(0, 100) > selected_move.accuracy:
            print("{}'s {} missed!".format(player_pokemon.name, selected_move.name))
            return

        # Check for type advantage/disadvantage
        effectiveness = self.check_effectiveness(selected_move.type, opponent_pokemon.types)

        # Calculate base damage
        base_damage = (((2 * player_pokemon.level) / 5) + 2) * selected_move.power * (
                player_pokemon.attack / opponent_pokemon.defense) / 50 + 2

        # Check for moves that have different effects based on the user's or the target's stat levels
        if selected_move.name in ["Belly Drum", "Flail", "Reversal"]:
            if selected_move.name == "Belly Drum":
                if player_pokemon.hp <= player_pokemon.max_hp / 2:
                    player_pokemon.attack *= 2
                    print("{}'s attack greatly rose!".format(player_pokemon.name))
                else:
                    print("{}'s HP is too high to use Belly Drum!".format(player_pokemon.name))
                    return
            elif selected_move.name == "Flail":
                player_pokemon_hp_ratio = player_pokemon.hp / player_pokemon.max_hp
                if player_pokemon_hp_ratio <= 0.5:
                    base_damage *= 2
                elif player_pokemon_hp_ratio <= 0.25:
                    base_damage *= 4
                else:
                    base_damage *= 0.5
            elif selected_move.name == "Reversal":
                player_pokemon_hp_ratio = player_pokemon.hp / player_pokemon.max_hp
                if player_pokemon_hp_ratio <= 0.5:
                    base_damage *= 2
                else:
                    base_damage *= 0.5
        # Apply effectiveness and random factor
        damage = int(base_damage * effectiveness * random.uniform(0.85, 1))

        # Inflict damage on opponent's Pokemon
        opponent_pokemon.hp -= damage
        print("{} used {} and dealt {} damage to {}. {} has {} HP left.".format(player_pokemon.name,
                                                                                selected_move.name, damage,
                                                                                opponent_pokemon.name,
                                                                                opponent_pokemon.name,
                                                                                opponent_pokemon.hp))

        # Check for moves with secondary effects such as chance of inflicting a status condition
        if selected_move.status_chance:
            if random.randint(0, 100) <= selected_move.status_chance:
                opponent_pokemon.status = selected_move.status
                print("{} was inflicted with {} status!".format(opponent_pokemon.name, selected_move.status))

        # Check for fainting
        if opponent_pokemon.hp <= 0:
            opponent_pokemon.faint()
    def player_switch(self):
        pass

    def player_use_item(self):
        pass

    def player_run(self):
        pass

    def opponent_attack(self):
        pass
