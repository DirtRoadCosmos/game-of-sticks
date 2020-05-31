from random import randint

# display intro info
print()
print("**********************************")
print("*   Welcome to Game of Sticks!   *")
print("**********************************")
print()
print("Your goal is to force the other ")
print("player to pick up the last stick.")

# create state variables
sticks = 21
player = 1
player_type = ["", ""]

print()
player_type[0] == ""
while not(player_type[0] == "ai" or player_type[0] == "human"):
    player_type[0] = input("Will Player 1 be AI or Human? ").lower()

player_type[1] == ""
while not(player_type[1] == "ai" or player_type[1] == "human"):
    player_type[1] = input("Will Player 2 be AI or Human? ").lower()

while sticks > 0:
    # print start of turn
    print()
    print(f"Player {player}: It's your turn.")
    print(f"There are {sticks} sticks on the table.")

    if player_type[player-1] == "human":
        # get player input
        pickup = input("How many sticks do you take? ")
        while not pickup.isdigit() or int(pickup) < 1 or int(pickup) > 3:
            pickup = input("How many sticks do you take? ")
        pickup = int(pickup)
    else:
        pickup = randint(1, 3)
        print(f"AI picks up {pickup} sticks.")

    # update state variables
    sticks = sticks - pickup
    if player == 1:
        player = 2
    elif player == 2:
        player = 1

print()
print(" --> That's the end!")
print(f"The winner is Player {player}!")


# DONE: repeat turns until we're done
# DONE: end the game
# DONE: validate user input





