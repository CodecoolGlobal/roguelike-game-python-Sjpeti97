import util
import engine
import ui
import rouge_like_storymode
import random

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def check_coordinate():
    check_door()
    check_item()
    pass


def all_items():
    items = {"🍞": 25, "🪓": 1, "🏹": 1, "🌀": 1, "🔰": 25, "💍": 1}
    return items


def check_door(player):
    if player["Player_position"][1] == 0:
        player["Player_position"][2] -= 1
        player["Player_position"][1] = 28

    elif player["Player_position"][1] == 29:
        player["Player_position"][2] += 1
        player["Player_position"][1] = 1


def get_enemy_movement(board, enemy, player_icon):
    possible_moves = []
    grounds = ["🟩", "🟫"]
    enemies = ["🐻", "🐉"]

    if board[enemy[0]-1][enemy[1]] == grounds[enemy[2]] or board[enemy[0]-1][enemy[1]] == player_icon:
        possible_moves.append("W")

    if board[enemy[0]+1][enemy[1]] == grounds[enemy[2]] or board[enemy[0]+1][enemy[1]] == player_icon:
        possible_moves.append("S")

    if board[enemy[0]][enemy[1]-1] == grounds[enemy[2]] or board[enemy[0]][enemy[1]-1] == player_icon:
        possible_moves.append("A")

    if board[enemy[0]][enemy[1]+1] == grounds[enemy[2]] or board[enemy[0]][enemy[1]+1] == player_icon:
        possible_moves.append("D")

    move = possible_moves[random.randint(0, len(possible_moves)-1)]
    new_coordinate, old_coordinate = get_movement(move, enemy)

    enemy = new_coordinate
    board[old_coordinate[0]][old_coordinate[1]] = grounds[old_coordinate[2]]
    board[new_coordinate[0]][new_coordinate[1]] = enemy[3]


def get_enemy_coordinate(boards):
    enemies = ["🐻", "🐉", "👴", "👁️"]
    enemy_coordinate = []
    for board in range(len(boards)):
        temp_coordinates = []
        for row in range(len(boards[board])):
            for column in range(len(boards[board][row])):
                if boards[board][row][column] == enemies[board]:
                    temp_coordinates.append([row, column, board, enemies[board]])

        enemy_coordinate.append(temp_coordinates)

    return enemy_coordinate


def get_movement(key, current_coordinate):
    old_coordinate = current_coordinate.copy()
    valid_inputs = ["W", "A", "S", "D"]
    if key.upper() in valid_inputs:
        if key.upper() == "W":
            current_coordinate[0] -= 1
        elif key.upper() == "A":
            current_coordinate[1] -= 1
        elif key.upper() == "S":
            current_coordinate[0] += 1
        elif key.upper() == "D":
            current_coordinate[1] += 1

    return current_coordinate, old_coordinate


def player_movement(board, player, key):
    new_coordinate, old_coordinate = get_movement()
    #if check_movement(board, player):


def check_movement(board, player):
    obstacles_with_door = ["🏠", "🌻", "🌳", "🍄", "🌋", "🔥", "🚪"]
    obstacles_without_door = ["🏠", "🌻", "🌳", "🍄", "🌋", "🔥"]
    if player["Inventory"]["💍"] > player["Player_position"][2]:
        obstacles = obstacles_without_door
    else:
        obstacles = obstacles_with_door

    if board[player["Player_position"][0]][player["Player_position"][1]] in obstacles:
        return False
    else:
        return True


def check_item(board, player):
    items = all_items()
    board_position = board[player["Player_position"][0]][player["Player_position"][1]]
    if board_position in items:
        if board_position == "🍞":
            player["Health"] += items["🍞"]
            if player["Health"] > player["Max_health"]:
                player["Health"] = player["Max_health"]
        elif board_position == "🪓":
            player["Inventory"]["🪓"] += 1
        elif board_position == "🏹":
            player["Inventory"]["🏹"] += 1
        elif board_position == "🌀":
            player["Inventory"]["🌀"] += 1
        elif board_position == "🔰":
            player["Armor"] += items["🔰"]
        elif board_position == "💍":
            player["Inventory"]["💍"] += 1


def get_player_character():
    print("""
    [1]Frodo Baggins 🧑
    [2]Legolas Greenleaf 🧝 
    [3]Gandalf 🧙
    """)

    character = int(input("Choose your character: "))

    if character == 1:
        return "🧑", 100, 100
    elif character == 2:
        return "🧝", 75, 75
    elif character == 3:
        return "🧙", 50, 50


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''

    name = input("Player's name: ")
    inventory = {"🪓": 0, "🏹": 0, "🌀": 0, "💍": 0}
    player_icon, health, max_health = get_player_character()
    player = {"Player_icon": player_icon, "Player_position": [PLAYER_START_X, PLAYER_START_Y, 0], "Player_name": name, "Health": health, "Armor": 0, "Max_health": max_health, "Inventory": inventory}

    return player


def main():
    util.clear_screen()
    #rouge_like_storymode.story()
    old_coordinate = [PLAYER_START_X, PLAYER_START_Y, 0]
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    util.clear_screen()
    is_running = True
    enemy_coordinates = get_enemy_coordinate(board)
    while is_running:
        old_health = player["Health"]
        old_armor = player["Armor"]
        if check_movement(board[player["Player_position"][2]], player):
            check_door(player)
            check_item(board[player["Player_position"][2]], player)
            engine.common_enemy_figth(player, board, enemy_coordinates[player["Player_position"][2]])
            engine.put_player_on_board(board[player["Player_position"][2]], player, old_coordinate, old_health, old_armor)
        else:
            player["Player_position"][0], player["Player_position"][1] = old_coordinate[0], old_coordinate[1]
            engine.put_player_on_board(board[player["Player_position"][2]], player, old_coordinate, old_health, old_armor)

        ui.display_board(board[player["Player_position"][2]])
        line = ""
        for item, value in player["Inventory"].items():
            line += f"{item}: {value} "
        print(line)
        print(f"🧡: {player['Health']}  🔰: {player['Armor']}")

        key = util.key_pressed()
        if key.upper() == 'Q':
            is_running = False
        elif key.upper() == "I":
            pass
        else:
            player["Player_position"], old_coordinate = get_movement(key, player["Player_position"])
            if player["Player_position"][2] < 2:
                for coordinate in enemy_coordinates[player["Player_position"][2]]:
                    get_enemy_movement(board[player["Player_position"][2]], coordinate, player["Player_icon"])
        util.clear_screen()
        if player["Health"] == 0:
            is_running = False
            print("Game Over!")

if __name__ == '__main__':
    main()
#🐲👁️         