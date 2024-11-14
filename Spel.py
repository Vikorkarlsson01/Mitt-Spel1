# Start
# Färg
import colorama
from colorama import Fore, Back, Style
colorama.init()

import random

# Spelet intro
def intro():
    print(Fore.BLUE + "Välkommen Till Gladiator Spelet")
    print(Style.RESET_ALL + "\nDu befinner dig på Colosseums sandiga arena, där publikens jubel ekar högt.")
    print("Här kämpar endast de modigaste krigarna om ära och överlevnad.")
    print(Fore.RED + "Du står nu ansikte mot ansikte med en annan gladiator, redo att slåss för ditt liv.")
    print(Style.RESET_ALL + "Endast en kan stå som segrare. Är du redo att möta ditt öde?")
    print(Fore.GREEN + "\nFörbered dig. " + Fore.RED + "Din strid börjar nu!" + Style.RESET_ALL + "")

player_health = 100
opponent_health = 100
round_number = 1

# Player_attack
def player_attack():
    global opponent_health
    print(Fore.BLUE + "\nVälj ditt anfall:")
    print(Fore.WHITE + "Slag. " + Fore.MAGENTA + "(50% träffchans, skada: 10-20)")
    print(Fore.WHITE + "Spark. " + Fore.MAGENTA + "(30% träffchans, skada: 15-30)")
    print(Fore.WHITE + "Kniv. " + Fore.MAGENTA + "(15% träffchans, skada: 30-50)")
    choice = input ("" + Fore.WHITE + "Ditt val " + Fore.GREEN + "Slag "
     + Fore.WHITE + ", " + Fore.GREEN + "Spark: " + Fore.WHITE + "eller " + Fore.GREEN + "Kniv " + Style.RESET_ALL ).lower()

# Slag/Spark och chans att träffa
    if choice == "slag":
        if random.randint(1, 100) <= 50: 
            damage = random.randint(10, 20)
            opponent_health -= damage
            print(f"Du träffar med ett slag och orsakar {Fore.RED}{damage}{Style.RESET_ALL} skada!")
        else:
            print(Fore.RED + "Ditt slag missar!")
    elif choice == "spark":
        if random.randint(1, 100) <= 30:
            damage = random.randint(15, 30)
            opponent_health -= damage
            print(f"Du träffar med en spark och orsakar {Fore.RED}{damage}{Style.RESET_ALL} skada!")
        else:
            print(Fore.RED + "Din spark missar!" + Style.RESET_ALL)
    elif choice == "kniv":
        if random.randint(1, 100) <= 15:
            damage = random.randint(30, 50)
            opponent_health -= damage
            print(f"Du träffar med en kniv och orsakar {Fore.RED}{damage}{Style.RESET_ALL} skada!")
        else:
            print(Fore.RED + "Din kniv missar!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Ogiltigt val," + Style.RESET_ALL + "du missar din chans att anfalla!")

# Opponent_attack
def opponent_attack():
    global player_health

    choice = random.choice(["slag", "spark"])

# Slag/Spark/kniv och chans att träffa
    if choice == "slag":
        if random.randint(1, 100) <= 50: 
            damage = random.randint(10, 20)
            player_health -= damage
            print(Style.RESET_ALL + f"Motståndaren träffar med ett slag och orsakar {Fore.RED}{damage}{Style.RESET_ALL} skada!")
        else:
            print(Style.RESET_ALL + "Motståndarens slag missar!")
    elif choice == "spark":
        if random.randint(1, 100) <= 30:
            damage = random.randint(15, 30)
            player_health -= damage
            print(f"Motståndaren träffar med en spark och orsakar {Fore.RED}{damage}{Style.RESET_ALL} skada!")
        else:
            print(Style.RESET_ALL + "Motståndarens spark missar!")
    elif choice == "kniv":
        if random.randint(1, 100) <= 15:
            damage = random.randint(30, 50)
            player_health -= damage
            print(f"Motståndaren träffar med en kniv och orsakar {Fore.RED}{damage}{Style.RESET_ALL} skada!")
        else:
            print(Fore.RED + "Motståndarens kniv missar!" + Style.RESET_ALL)

# Kollar vem som vinner
def check_winner():
    if player_health <= 0:
        print(Fore.RED + "\nDu har blivit besegrad! Motståndaren vinner striden.")
        return True
    elif opponent_health <= 0:
        print(Fore.GREEN + "\nGrattis! Du har besegrat din motståndare och vunnit striden!")
        return True
    return False

# Vilken hälsa man har
def game():
    intro()
    while True:
        print(f"\nDin hälsa: {Fore.GREEN}{player_health}{Style.RESET_ALL} | Motståndarens hälsa: {Fore.RED}{opponent_health}{Style.RESET_ALL}")
        player_attack()
        
        if check_winner():
            break
        
        opponent_attack()
        
        if check_winner():
            break

# Villken rounda det är 
def game():
    global round_number
    intro()
    while True:
        print(f"\n---Runda {round_number}---")
        print(f"Din hälsa: {Fore.GREEN}{player_health}{Style.RESET_ALL} | Motståndarens hälsa: {Fore.RED}{opponent_health}{Style.RESET_ALL}")
        player_attack()
        
        if check_winner():
            break
        
        opponent_attack()
        
        if check_winner():
            break

        round_number += 1

game()

# Färg
colorama.deinit()