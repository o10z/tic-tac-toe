# Initialize the game
print("Tic Tac Toe")
grid = "-1-|-2-|-3-\n" \
       "-4-|-5-|-6-\n" \
       "-7-|-8-|-9-\n"

# Player icons 'X' and 'O'
player_1 = "X"
player_2 = "O"

# List to keep track of positions Players
player_1_list = []
player_2_list = []

# List of all possible winning combinations
possible_wins = [
    ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],
    ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
    ['1', '5', '9'], ['3', '5', '7']
]


# Function to plot player's move on the game grid
def plot(player_icon, player_list):
    global grid
    print(grid)
    grid_position = input(f"Player '{player_icon}' where do you want to plot: ")
    # Check if the input is valid
    if grid_position.isdigit() and 1 <= int(grid_position) <= 9:
        if grid_position in player_1_list or grid_position in player_2_list:
            print("Position already occupied...")
            plot(player_icon, player_list)
        else:
            grid = grid.replace(grid_position, player_icon, 1)
            player_list.append(grid_position)
    else:
        print("Invalid input...")
        plot(player_icon, player_list)


# Function to determine if either players have won
def winner(player_icon, player_list):
    for win_combination in possible_wins:
        if all(elem in player_list for elem in win_combination):
            print(f"Player {player_icon} has won!")
            return True
    return False


# loops for the total amount of rounds tic-tac-toe last for
for rounds in range(1, 10):
    # determines which player turn it is
    player = ""
    if rounds % 2:
        player = player_2
        plist = player_2_list
    else:
        player = player_1
        plist = player_1_list
    plot(player, plist)
    # the shortest a player could win is 5 rounds
    # if a win is not found it would be a draw
    if rounds >= 5 and winner(player, plist):
        break
    elif rounds == 9:
        print("DRAW")
print(grid)
