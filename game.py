from random import randint
import time

starting_sticks = 21
playing = True
training_total = 599
training_todo = 0
wins = [0, 0]
hats = [[], []]
waiting = [[], []]
hide = False
seen_ai_training = False

# display intro info
print()
print("**********************************")
print("*   Welcome to Game of Sticks!   *")
print("**********************************")
print()
print("Your goal is to force the other ")
print("player to pick up the last stick.")

player_type = ["", ""]
player_name = ["", ""]

print()
playmode = -1
while not(playmode in [0, 1, 2]):
    print("How would you like to play?")
    print(" (0) Human vs AI")
    print(" (1) Human vs Random")
    print(" (2) Human vs Human")
    playmode = int(input("Select 0, 1, or 2: "))

if playmode == 0:
    player_type[0] = "h"
    player_type[1] = "a"
    player_name[0] = "Human"
    player_name[1] = "AI"
    print()
    print()
    print()
    print()
    print("*****************************")
    print(" AI will now play >500 games")
    print(" against itself")
    print(" to figure out a strategy")
    print(" ... press enter ...")
    print("*****************************")
    input()
    print("playing ")
    for i in range(10):
        time.sleep(.2)
        print("."*(i+1))

elif playmode == 1:
    player_type[0] = "h"
    player_type[1] = "r"
    player_name[0] = "Human"
    player_name[1] = "Random"
elif playmode == 2:
    player_type[0] = "h"
    player_type[1] = "h"
    print()
    player_name[0] = input("What is Player 1's name? ")
    player_name[1] = input("What is Player 2's name? ")

orig_type=[]
if "a" in player_type:
    orig_type.append(player_type[0])
    orig_type.append(player_type[1])
    player_type[0] = "a"
    player_type[1] = "a"
    training_todo = training_total
    playing = False
    hide = True

def full_hat(i):
    if i == 0:
        return [1]
    elif i == 1:
        return [1, 2]
    else:
        return [1, 2, 3]

for i in range(starting_sticks):
    hats[0].append(full_hat(i))
    hats[1].append(full_hat(i))
    waiting[0].append(0)
    waiting[1].append(0)

while playing or training_todo > 0:
    sticks = starting_sticks
    player = 1
    printing = False
    if not hide and (playing or
        training_todo > training_total - 5 or
        (training_todo > training_total - 100 and training_todo % 10 == 0) or
        training_todo % 100 == 0):
        printing = True

    while sticks > 0:
        # print start of turn
        if printing:
            print()
            print(f"There are {sticks} sticks on the table.")
            if player_type[player-1] == "h":
                print(f"It's Player {player}: {player_name[player-1]}'s turn.")
            else:
                print(f"It's Player {player}'s turn.")

        max = min(sticks, 3)
        if player_type[player-1] == "r":
            pickup = randint(1, max)
            if printing: print(f"Random picks up {pickup} sticks.")
        elif player_type[player-1] == "a":
            options = hats[player-1][sticks-1]
            if printing and not playing: print(f"AI options are {options}")
            pickup = options.pop(randint(0, len(options)-1))
            waiting[player-1][sticks-1] = pickup
            if printing: print(f"AI picks up {pickup} sticks.")
        elif player_type[player-1] == "h":
            pickup = input(f"How many sticks do you take? (1-{max}) ")
            while not pickup.isdigit() or int(pickup) < 1 or int(pickup) > max:
                pickup = input(f"How many sticks do you take? (1-{max}) ")
            pickup = int(pickup)

        # update state variables
        sticks = sticks - pickup
        if player == 1:
            player = 2
        elif player == 2:
            player = 1

    if printing:
        print()
        print(" --> That's the end <--")
        if training_todo > 0:
            print(f"The winner is Player {player}: AI!")
        else:
            print(f"The winner is Player {player}: {player_name[player-1]}!")

    # update winning AI
    if player_type[player-1] == "a":
        for idx, item in enumerate(waiting[player-1]):
            if item != 0:
                hats[player-1][idx].extend([item, item])

    # for both players
    for i in range(2):
        if player_type[i] == "a":
            # clear waiting
            for j in range(starting_sticks):
                waiting[i][j] = 0
            # fill empty hats
            for idx, hat in enumerate(hats[i]):
                if len(hat) == 0:
                    hat.extend(full_hat(idx))
            # print hats
            if printing and not playing:
                print()
                print(f"Updated hats for Player {i+1}:")
                for idx, hat in enumerate(reversed(hats[i])):
                    print(f"Hat {21-idx if idx < 12 else '0'+str(21-idx)}: {hat}")

    wins[player-1] += 1
    if printing:
        print()
        print(f"Games Played:  {wins[0]+wins[1]}")
        print(f"Current Score: {wins[0]}-{wins[1]}")

    if playing:
        if playmode == 0 and not seen_ai_training:
            print()
            watch = input("Press ENTER to play again,\nor 'w' to erase the AI's memory and watch it train. ")
            print()
            if watch == "w":
                wins = [0, 0]
                player_type[0] = "a"
                player_type[1] = "a"
                training_todo = training_total
                playing = False
                hide = False
                hats = [[], []]
                waiting = [[], []]
                seen_ai_training = True
                for i in range(starting_sticks):
                    hats[0].append(full_hat(i))
                    hats[1].append(full_hat(i))
                    waiting[0].append(0)
                    waiting[1].append(0)
        else:
            print()
            again = input("Press ENTER to play again,\nor 'e' to exit. ")
            print()
            if again == "e":
                playing = False
    else:
        # training update
        if training_todo > 1:
            training_todo -= 1
            if printing:
                print("Scroll up to see game history.")
                input("Then press ENTER.")
                print()
        elif training_todo == 1:
            training_todo = 0
            playing = True
            hide = False
            player_type[0]=orig_type[0]
            player_type[1]=orig_type[1]
            wins = [0, 0]

            print()
            print("*****************************")
            print("  just played more >500 games")
            print("  AI training complete")
            print("  Ready to play a human")
            print("  ... press enter ...")
            print("*****************************")
            print()
            input()


