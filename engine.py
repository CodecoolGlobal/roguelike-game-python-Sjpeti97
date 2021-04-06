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
    gate = []
    index_of_objects = 0
    objects = ["🟩", "🏠", "🚪", "🟫", "🌳", "🚪", "⬛", "🌋", "🚪" ]
    for number in range(3):
        wall = []
        board = []
        for _ in range(width):
            wall.append(objects[index_of_objects + 1])
        board.append(wall.copy())
        gate.append(random.randint(1, height-3))
        for column in range(height-2):
            row = []
            for index in range(width):
                if column == gate[number] and index == width-1 and number != 2:
                    row.append(objects[index_of_objects + 2])
                elif index == 0 or index == width-1:
                    row.append(objects[index_of_objects + 1])
                else:
                    row.append(objects[index_of_objects + 0])
            board.append(row.copy())
        if number != 0:
            board[gate[number-1]+1][0] = "🚪"
        board.append(wall.copy())
        set_of_levels.append(board.copy())
        index_of_objects += 3
    return set_of_levels


def create_obstacles_in_boards(set_of_boards, width=30, heigth=20):
    obstacles = ["🌻", "🍄", "🔥"]
    directions = ["h", "v"]
    for number in range(len(set_of_boards)):
        numbers_of_obstacles = (width*heigth)//5
        while numbers_of_obstacles > 0:
            obstacle_coordinate_x = random.randint(1, width-2)
            obstacle_coordinate_y = random.randint(1, heigth-2)
            direction = random.choice(directions)
            if direction == "h":
                for count in range(3):
                    if obstacle_coordinate_x in range(width-4, width-1):
                        set_of_boards[number][obstacle_coordinate_y][obstacle_coordinate_x - count] = obstacles[number]
                        numbers_of_obstacles -= 1
                    else:
                        set_of_boards[number][obstacle_coordinate_y][obstacle_coordinate_x + count] = obstacles[number]
                        numbers_of_obstacles -= 1
            if direction == "v":
                for count in range(3):
                    if obstacle_coordinate_y in range(heigth-4, heigth - 1):
                        set_of_boards[number][obstacle_coordinate_y - count][obstacle_coordinate_x] = obstacles[number]
                        numbers_of_obstacles -= 1
                    else:
                        set_of_boards[number][obstacle_coordinate_y + count][obstacle_coordinate_x] = obstacles[number]
                        numbers_of_obstacles -= 1
    return set_of_boards


                        


def display_board(boards):
    for board in boards:
        for row in board:
            print("".join(row))

display_board(create_obstacles_in_boards(create_board(30, 20)))

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
