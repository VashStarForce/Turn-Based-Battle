import random

def main():

    print("You've reached the end of a journey across the Weyward continent of the floating world.")
    print("You head to a small secluded island of the floating world at the end of the spilling water.")
    print("You now face off against Dullahan, the Headless Knight!")


    print("\nEither type in the name of the attack or the corresponding number"
          "\nThe player and Computer/Dullahan will take turns attacking. Every attack and heal will have a range.")

    print("Now let the battle begin! The wheels of fate are turning once again. "
          "\n(To select a move to use, type the corresponding number.)")

    play_again = True

    # Sets up the play again loop
    while play_again:
        victor = None
        # 5,000,000
        player_hp = 5000000
        # 10,000,000
        Dullahan_hp = 10000000

        # Randomly pick who goes first
        turn = random.randint(1,2) # heads or tails
        if turn == 1:
            player_turn = True
            Dullahan_turn = False
            print("\nPlayer will go first.")
        else:
            player_turn = False
            Dullahan_turn = True
            print("\nDullahan will go first.")


        print("\nPlayer health: ", player_hp, "Dullahan health: ", Dullahan_hp)

        # Sets up the main game loop
        while (player_hp != 0 or Dullahan_hp != 0):

            heal_up = False  # determine if heal has been used and resets false each loop.

            # List of moves that can be used and the contains the number range for each.
            moves = {"Sol Blade": random.randint(40300, 93400),
                     "Grand Gaia": random.randint(238900, 350000),
                     "Grand Heal": random.randint(400000, 700000),
                     "Planet Diver": random.randint(239800, 312700),
                     "Astral Impact": random.randint(238400, 300000),
                     "Turn Up: Showtime": random.randint(300000, 350000),
                     "Turn Up: Sabre Dance": random.randint(300000, 375000),
                     "Turn Up: Joker": random.randint(300000, 400000),
                     "Turn Up: Transcendence Strike": random.randint(300000, 700000),
                     "Megaera": random.randint(400000, 650000),
                     "Iris": random.randint(400000, 650000),
                     "Crystallux": random.randint(400000, 650000),
                     "Charon": random.randint(400000, 650000),
                     "Flora": random.randint(400000, 650000),
                     "Condemn": random.randint(300000, 600000),
                     "Miasma Extract": random.randint(500000, 8000000),
                     "Dark Contact": random.randint(300000, 700000),
                     "Fulminous Edge": random.randint(400000, 700000),
                     "Calamity Collapse": random.randint(5000000, 6000000)}

            if player_turn:
                print("\nPlease select a move:"
                      "\n1. Attack with the Sol Blade."
                      "\n2. Cast Grand Gaia."
                      "\n3. Cast Grand Heal."
                      "\n4. Cast Planet Diver."
                      "\n5. Cast Astral Impact."
                      "\n6. Insert the Turn Up: Showtime card into the Sol Blade."
                      "\n7. Insert the Turn Up: Sabre Dance card into the Sol Blade."
                      "\n8. Insert the Turn Up: Joker card into the Sol Blade."
                      "\n9. Insert the Turn Up: Transcendence Strike card into the Sol Blade."
                      "\n10. Summon Megaera."
                      "\n11. Summon Iris."
                      "\n12. Summon Crystallux."
                      "\n13. Summon Charon."
                      "\n14. Summon Flora.")


                player_move = input("> ").lower()

                if player_move in ("1", "Sol Blade"):
                    player_move = moves["Sol Blade"]
                    print("\nYou slashed Dullahan with the Sol Blade. It dealt ", player_move, " damage.")
                elif player_move in ("2", "Grand Gaia"):
                    player_move = moves["Grand Gaia"]
                    print("\nYou cast Grand Gaia. "
                          "\nThe ground beneath Dullahan erupts in pillars of energy."
                          "\nIt dealt ", player_move, " damage.")
                elif player_move in ("3", "Grand Heal"):
                    heal_up = True  # heal activated/goes off
                    player_move = moves["Grand Heal"]
                    print("\nYou cast Grand Heal. It healed for ", player_move, " health.")
                elif player_move in ("4", "Planet Diver"):
                    player_move = moves["Planet Diver"]
                    print("\nYou cast Planet Diver. "
                          "\nYou jumped into the air and crashed into Dullahan with your sword."
                          "\nIt dealt ", player_move, " damage.")
                elif player_move in ("5", "Astral Impact"):
                    player_move = moves["Astral Impact"]
                    print("\nYou cast Astral Impact. "
                          "\nYou jump and slam the Sol Blade into Dullahan with the power of the stars above."
                          "\nIt dealt ", player_move, " damage.")
                elif player_move in ("6", "Turn Up: Showtime"):
                    player_move = moves["Turn Up: Showtime"]
                    print("\nSol Blade: Turn up!"
                          "\nYou disappear behind a dropping red curtain, reappear behind Dullahan and pierce his armor after inserting the Showtime card into the Sol Blade."
                          "\nIt dealt ", player_move, " damage.")
                elif player_move in ("7", "Turn Up: Sabre Dance"):
                    player_move = moves["Turn Up: Sabre Dance"]
                    print("\nSol Blade: Turn up!"
                          "\nYou dance around Dullahan cutting, slash, stabbing, and thrusting at him with the Sol Blade after inserting the Sabre Dance card into the sword."
                          "\nIt dealt ", player_move, " damage.")
                elif player_move in ("8", "Turn Up: Joker"):
                    player_move = moves["Turn Up: Joker"]
                    print("\nSol Blade: Turn up!"
                          "\nYou punch Dullahan applying a crushing pressure to his armor after inserting the Joker card into the Sol Blade."
                          "\nIt dealt ", player_move, " damage.")
                elif player_move in ("9", "Turn Up: Transcendence Strike"):
                    player_move = moves["Turn Up: Transcendence Strike"]
                    print("\nSol Blade: Turn up!"
                          "\nYou slash Dullahan with destructive force after inserting the Transcendence Strike card into the Sol Blade."
                          "\nIt dealt ", player_move, " damage.")
                elif player_move in ("10", "Megaera"):
                    player_move = moves["Megaera"]
                    print("\nYou summoned Megaera from Greek Mythology, dropping four large swords and engulfing Dullahan in an explosion. "
                      "\nIt dealt ", player_move, " damage.")
                elif player_move in ("11", "Iris"):
                    player_move = moves["Iris"]
                    print("\nYou summoned Iris from Greek Mythology, who sends and projects Dullahan into space before sending him into the sun."
                    "\nIt dealt ", player_move, " damage.")
                elif player_move in ("12", "Crystallux"):
                    player_move = moves["Crystallux"]
                    print("\nYou summoned Crystallux, a chandelier-like dragon emerges from above and showers Dullahan in a blazing light."
                    "\nIt dealt ", player_move, " damage.")
                elif player_move in ("13", "Charon"):
                    player_move = moves["Charon"]
                    print("\nYou summoned Charon, a skeletal entity and casts a flow of dark mud towards Dullahan that hardens and shatters."
                    "\nIt dealt ", player_move, " damage.")
                elif player_move in ("14", "Flora"):
                    player_move = moves["Flora"]
                    print("\nYou summoned Flora, from Roman Mythology who rains down magical rose blossoms that exlode upon hitting Dullahan."
                    "\nIt dealt ", player_move, " damage.")
                else:
                    print("\nThat is not a valid move. Please type it corectly or use the corresponding number.")
                    continue

            else:  # Dullahan turn

                if Dullahan_hp > 30000:
                    if player_hp > 75000:
                        Dullahan_move = moves["Condemn"]
                        print("\nThe Dullahan used Condemn and you feel a sharp pain throughout your body."
                        "\nIt dealt ", Dullahan_move, " damage.")
                    elif player_hp > 35000 and player_hp <= 75000:  # Dullahan decides whether keep fighting or be slightly cautious
                        imoves = ["Fulminous Edge", "Calamity Collapse"]
                        imoves = random.choice(imoves)
                        Dullahan_move = moves[imoves]
                        print("\nThe Dullahan used ", imoves, ". It dealt ", Dullahan_move, " damage.")
                    elif player_hp <= 35000:
                        Dullahan_move = moves["Dark Contact"]  # Attempt to finish off the player
                        print("\nThe Dullahan used Dark Contact and attempts to kill you by surronding you with miasma and slashing you."
                        "\nIt dealt ", Dullahan_move, " damage.")
                else:  # if the Dullahan has less than 30,000 health, there is a 50% chance they will heal
                    heal_or_fight = random.randint(1, 2)
                    if heal_or_fight == 1:
                        heal_up = True
                        Dullahan_move = moves["Miasma Extract"]
                        print("\nThe Dullahan used Miasma Extract. Dullahan healed for ", Dullahan_move, " health.")
                    else:
                        if player_hp > 75000:
                                Dullahan_move = moves["Crystallux"]
                                print("\nThe Dullahan used Crucible. It dealt ", Dullahan_move, " damage.")
                        elif player_hp > 35000 and player_hp <= 75000:
                                imoves = ["Calamity Collapse", "Fulminous Edge"]
                                imoves = random.choice(imoves)
                                Dullahan_move = moves[imoves]
                                print("\nThe Dullahan used ", imoves, ". It dealt ", Dullahan_move, " damage.")
                        elif player_hp <= 35000:
                                Dullahan_move = moves["Dark Contact"]  # Attempt to finish off the player
                                print("\nThe Dullahan used Condemn and you feel a sharp pain throughout your body."
                                "\nIt dealt ", Dullahan_move, " damage.")

            if heal_up:
                if player_turn:
                    player_hp += player_move
                    if player_hp > 5000000:
                        player_hp = 5000000  # cap max health at 5000000. No over healing!
                else:
                    Dullahan_hp += Dullahan_move
                    if Dullahan_hp > 10000000:
                        Dullahan_hp = 10000000
            else:
                if player_turn:
                    Dullahan_hp -= player_move
                    if Dullahan_hp < 0:
                        Dullahan_hp = 0  # cap minimum health at 0
                        victor = "Player"
                        break
                else:
                    player_hp -= Dullahan_move
                    if player_hp < 0:
                        player_hp = 0
                        victor = "Dullahan"
                        break

            print("\nPlayer health: ", player_hp, "\nDullahan health: ", Dullahan_hp)

            # switch turns
            player_turn = not player_turn
            Dullahan_turn = not Dullahan_turn

        # Once main game's while loop breaks, display text based on who wins

        if victor == "Player":
            print("\nPlayer health: ", player_hp, "Dullahan health: ", Dullahan_hp)
            print("\nYou have defeated Dullahan. You have obtained Excalibur.")
        else:
            print("\nPlayer health: ", player_hp, "Dullahan health: ", Dullahan_hp)
            print("\nYou've been killed by Dullahan.")

        print("\nGo back in time and attempt again?")

        answer = input("> ").lower()
        if answer not in ("yes", "y"):
            play_again = False

main()