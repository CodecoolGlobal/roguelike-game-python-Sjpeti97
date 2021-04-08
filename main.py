import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20

def check_coordinate():
    check_door()
    check_item()
    check_enemy()
    pass

def all_items():
    items = {"🍞": 25, "🪓": True, "🏹": True, "🌀": True, "🔰": 25, "💍": 1}
    return items

def check_door(player):
    if player["Player_position"][1] == 0:
        player["Player_position"][2] -= 1
        player["Player_position"][1] = 28

    elif player["Player_position"][1] == 29:
        player["Player_position"][2] += 1
        player["Player_position"][1] = 1

def get_enemy_movement(board):
    pass

def get_movement(key, player_coordinate):
    old_coordinate = player_coordinate.copy()
    valid_inputs = ["W", "A", "S", "D"]
    if key.upper() in valid_inputs:
        if key.upper() == "W":
            player_coordinate[0] -= 1
        elif key.upper() == "A":
            player_coordinate[1] -= 1
        elif key.upper() == "S":
            player_coordinate[0] += 1
        elif key.upper() == "D":
            player_coordinate[1] += 1
    
    return player_coordinate, old_coordinate


def check_movement(board, player):
    obstacles_with_door = ["🏠", "🌻", "🌳", "🍄", "🌋", "🔥", "🚪"]
    obstacles_without_door = ["🏠", "🌻", "🌳", "🍄", "🌋", "🔥"]
    if player["Ring"] > player["Player_position"][2]:
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
            # board_position == " "
            player["Inventory"].append("🪓")
            if player["Player_icon"] == "🧑":
                player["Weapon"] = items["🪓"]
        elif board_position == "🏹":
            # board_position == " "
            player["Inventory"].append("🏹")
            if player["Player_icon"] == "🧝":
                player["Weapon"] == items["🏹"]
        elif board_position == "🌀":
            # board_position == " "
            player["Inventory"].append("🌀")
            if player["Player_icon"] == "🧙":
                player["Weapon"] == items["🌀"]
        
        elif board_position == "🔰":
            # board_position == " "
            player["Armor"] += items["🔰"]
        
        elif board_position == "💍":
            # board_position == " "
            player["Inventory"].append("💍")
            player["Ring"] += items["💍"]


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
    player_icon, health, max_health = get_player_character()
    player = {"Player_icon": player_icon, "Player_position": [PLAYER_START_X, PLAYER_START_Y, 0], "Player_name": name, "Health": health, "Armor": 0, "Max_health": max_health, "Ring": 0, "Weapon": False, "Inventory": []}
    
    return player


def main():
    old_coordinate = [PLAYER_START_X, PLAYER_START_Y, 0]
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    util.clear_screen()
    is_running = True
    while is_running:
        old_health = player["Health"]      
        if check_movement(board[player["Player_position"][2]], player):
            check_door(player)
            check_item(board[player["Player_position"][2]], player)
            engine.common_enemy_figth(player, board)
            engine.put_player_on_board(board[player["Player_position"][2]], player, old_coordinate, old_health)
        else:
            player["Player_position"][0], player["Player_position"][1] = old_coordinate[0], old_coordinate[1]
            engine.put_player_on_board(board[player["Player_position"][2]], player, old_coordinate, old_health)
        ui.display_board(board[player["Player_position"][2]])

        key = util.key_pressed()
        if key.upper() == 'Q':
            is_running = False
        elif key.upper() == "I":
            print(player["Inventory"]) 
        else:
            player["Player_position"], old_coordinate = get_movement(key, player["Player_position"])     

        util.clear_screen()

if __name__ == '__main__':
    main()
#🐲👁️