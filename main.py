import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def all_items():
    items = {"🍞": 25, "🗡️": True, "🏹": True, "🌀": True, "🛡️": 25, "💍": True}
    return items

def get_movement(key, player_coordinate):
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

    return player_coordinate

def check_movement(board, player):
    obstacles = ["🏠", "🌻", "🌳", "🍄", "🌋", "🔥"]
    #board_position = board[[player["Player_position"[0]]]], [player["Player_position"[1]]]
    position = player["Player_position"]
    board_position = board[position[0]][position[1]]
    print(board_position)
    # if board_position in obstacles:
    #     return True

def check_item(board, player):
    items = all_items()
    board_position = board[player["Player_position"][0]][player["Player_position"][1]]
    if board_position in items:
        if board_position == "🍞":
            player["Health"] += items["🍞"]
            board_position == " "
            if player["Health"] > player["Max_health"]:
                player["Health"] = player["Max_health"]
            
        elif board_position == "🗡️":
            board_position == " "
            player.update("Inventory" == "🗡️")
            if player["Player_icon"] == "🧑":
                player["Weapon"] == items["🗡️"]
        elif board_position == "🏹":
            board_position == " "
            player.update("Inventory" == "🏹")
            if player["Player_icon"] == "🧝":
                player["Weapon"] == items["🏹"]
        elif board_position == "🌀":
            board_position == " "
            player.update("Inventory" == "🌀")
            if player["Player_icon"] == "🧙":
                player["Weapon"] == items["🌀"]
        
        elif board_position == "🛡️":
            board_position == " "
            player["Armor"] += items["🛡️"]
        
        elif board_position == "💍":
            board_position == " "
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
    player = {"Player_icon": player_icon, "Player_position": [PLAYER_START_X, PLAYER_START_Y], "Player_name": name, "Health": health, "Armor": 0, "Max_health": max_health, "Ring": False, "Weapon": False, "Inventory": []}
    
    return player


def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    util.clear_screen()
    is_running = True
    while is_running:
        if check_movement(board, player) is False:
            engine.put_player_on_board(board[0], player)
        ui.display_board(board[0])

        key = util.key_pressed()
        if key.upper() == 'Q':
            is_running = False   
        elif key.upper() == "I":
            print(player["Inventory"]) 
        else:
            player["Player_position"] = get_movement(key, player["Player_position"])
            print(player)
            
    
        
        util.clear_screen()


if __name__ == '__main__':
    main()
#🐲👁️