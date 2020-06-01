from random import randint

# display intro info
print()
print("**********************************")
print("*   Welcome to Game of Sticks!   *")
print("**********************************")
print()
print("Your goal is to force the other ")
print("player to pick up the last stick.")

player_type = ["", ""]

print()
player_type[0] == ""
while not(player_type[0] in ["r", "a", "h"]):
    player_type[0] = input("Will Player 1 be (r)andom, (a)i or (h)uman? ").lower()

player_type[1] == ""
while not(player_type[1] in ["r", "a", "h"]):
    player_type[1] = input("Will Player 2 be (r)andom, (a)i or (h)uman? ").lower()

starting_sticks = 21
playing = True
wins = [0, 0]
hats = []
hats.append([])
hats.append([])
hats[1] = []
waiting = []
waiting.append([])
waiting.append([])

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

while playing:
    sticks = starting_sticks
    player = 1
    while sticks > 0:
        # print start of turn
        print()
        print(f"Player {player}: It's your turn.")
        print(f"There are {sticks} sticks on the table.")

        if player_type[player-1] == "r":
            pickup = randint(1, 3)
            print(f"Random picks up {pickup} sticks.")
        elif player_type[player-1] == "a":
            options = hats[player-1][sticks-1]
            print(f"AI options are {options}")
            pickup = options.pop(randint(0, len(options)-1))
            waiting[player-1][sticks-1] = pickup
            print(f"AI picks up {pickup} sticks.")
        elif player_type[player-1] == "h":
            # get player input
            pickup = input("How many sticks do you take? ")
            while not pickup.isdigit() or int(pickup) < 1 or int(pickup) > 3:
                pickup = input("How many sticks do you take? ")
            pickup = int(pickup)

        # update state variables
        sticks = sticks - pickup
        if player == 1:
            player = 2
        elif player == 2:
            player = 1

    print()
    print(" --> That's the end!")
    print(f"The winner is Player {player}!")
    wins[player-1] += 1
    print(f"That makes it {wins[0]}-{wins[1]}")

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
            print(waiting[i])
            # fill empty hats
            for idx, hat in enumerate(hats[i]):
                if len(hat) == 0:
                    hat.extend(full_hat(idx))
            # print hats
            print()
            print(f"Updated hats for Player {i+1}:")
            for idx, hat in enumerate(reversed(hats[i])):
                print(f"Hat {21-idx}: {hat}")

    print()
    again = input("Press ENTER to play again, q-ENTER to exit. ")
    print()
    if again == "q":
        playing = False





