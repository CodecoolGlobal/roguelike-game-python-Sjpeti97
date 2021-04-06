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
    if key.upper() in valid_inputs:
        if key.upper() == "W":
            player_coordinate[1] -= 1
        elif key.upper() == "A":
            player_coordinate[0] -= 1
        elif key.upper() == "S":
            player_coordinate[1] += 1
        elif key.upper() == "D":
            player_coordinate[0] += 1
    else:
        return

def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    pass


def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    player_coordinate = (PLAYER_START_X, PLAYER_START_Y)
    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()
