import random

def create_board(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    set_of_levels = []
    place_of_previous_gate = None
    index_of_objects = 0
    objects = ["🟩", "🏠", "🚪", "🟫", "🌳", "🚪", "⬛", "🔥", "🚪" ]
    for number in range(3):
        wall = []
        board = []
        for _ in range(width):
            wall.append(objects[index_of_objects + 1])
        board.append(wall.copy())
        gate = random.randint(1, height-2)
        for column in range(height-2):
            row = []
            for index in range(width):
                if index == 0 and number != 0 and column == place_of_previous_gate:
                    row.append(objects[index_of_objects + 2])
                elif column == gate and index == width-1 and number != 2:
                    place_of_previous_gate = column
                    row.append(objects[index_of_objects + 2])
                elif index == 0 or index == width-1:
                    row.append(objects[index_of_objects + 1])
                else:
                    row.append(objects[index_of_objects + 0])
            board.append(row.copy())
        board.append(wall.copy())
        set_of_levels.append(board.copy())
        index_of_objects += 3
    return set_of_levels

def display_board(boards):
    for board in boards:
        for row in board:
            print("".join(row))

display_board(create_board(30, 20))

def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    pass
