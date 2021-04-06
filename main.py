import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20

def get_movement(key, player_coordinate):
    valid_inputs = ["W", "A", "S", "D"]
    coordinate_x = player_coordinate[0]
    coordinate_y = player_coordinate[1]
    if key.upper() in valid_inputs:
        if key.upper() == "W":
            coordinate_y -= 1
        elif key.upper() == "A":
            coordinate_x -= 1
        elif key.upper() == "S":
            coordinate_y += 1
        elif key.upper() == "D":
            coordinate_x += 1
    else:
        return
    
    player_coordinate = (coordinate_x, coordinate_y)
    return player_coordinate

def get_player_character():
    print("""
    [1]Frodo Baggins 🧑
    [2]Legolas Greenleaf 🧝 
    [3]Gandalf 🧙
    """)
    
    character = int(input("Choose your character: "))
    
    if character == 1:
        return "🧑", 100
    elif character == 2:
        return "🧝", 75
    elif character == 3:
        return "🧙", 50

def create_player(player_coordinate):
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    
    name = input("Player's name: ")
    player_icon, health = get_player_character()
    player = {"Player_icon": player_icon, "Player_position": player_coordinate, "Player_name": name, "Health": health}
    
    return player


def main():
    player_coordinate = (PLAYER_START_X, PLAYER_START_Y)
    player = create_player(player_coordinate)
    print(player)
    # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    # util.clear_screen()
    # is_running = True
    # while is_running:
    #     engine.put_player_on_board(board, player)
    #     ui.display_board(board)

    #     key = util.key_pressed()
    #     if key.upper == 'Q':
    #         is_running = False
    #     else:
    #         pass
    #     util.clear_screen()


if __name__ == '__main__':
    main()
#🐲👁️