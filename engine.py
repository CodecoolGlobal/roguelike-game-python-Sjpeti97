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
    index_of_objects = 0
    objects = ["🟩", "🏠", "🚪", "🟫", "🌳", "🚪", "⬛", "🔥", "🚪" ]
    for number in range(3):
        wall = []
        board = []
        gate = random.randint(1, height-2)
        for _ in range(width):
            wall.append(objects[index_of_objects + 1])
        board.append(wall.copy())
        for column in range(height-2):
            row = []
            for index in range(width):
                if column == gate and (index == width-1 or index == 0):
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
