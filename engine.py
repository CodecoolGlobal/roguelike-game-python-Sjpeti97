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
    board = []
    objects = [" ", "🌳"]
    wall = []
    for num in range(width):
        wall.append(objects[1])
    board.append(wall.copy())
    for num in range(width-2):
        row = []
        for index in range(height):
            if index == 0 or index == height-1:
                row.append(objects[1])
            else:
                row.append(objects[0])
        board.append(row.copy())
    board.append(wall.copy())
    return board



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
