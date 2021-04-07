import random


def placing_items(set_of_boards, width=30, heigth=20):
    items = ["🍞", "🪓", "🏹", "🌀", "🔰", "💍"]
    for board in range(len(set_of_boards)):
        for index in range(len(items)):
            item_coordinate_x = random.randint(1, width-2)
            item_coordinate_y = random.randint(1, heigth-2)
            set_of_boards[board][item_coordinate_y][item_coordinate_x] = items[index]
    # for number in range(len(set_of_boards)):
    #     for


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
    objects = ["🟩", "🏠", "🚪", "🟫", "🌳", "🚪", "⬛", "🌋", "🚪"]
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
    create_obstacles_in_boards(set_of_levels)
    placing_items(set_of_levels)
    create_other_characters(set_of_levels)
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
                    if obstacle_coordinate_x in range(width-4, width-1) and check_gate(set_of_boards[number], obstacle_coordinate_x - count, obstacle_coordinate_y):
                        set_of_boards[number][obstacle_coordinate_y][obstacle_coordinate_x - count] = obstacles[number]
                        numbers_of_obstacles -= 1
                    elif check_gate(set_of_boards[number], obstacle_coordinate_x + count, obstacle_coordinate_y):
                        set_of_boards[number][obstacle_coordinate_y][obstacle_coordinate_x + count] = obstacles[number]
                        numbers_of_obstacles -= 1
            if direction == "v":
                for count in range(3):
                    if obstacle_coordinate_y in range(heigth-4, heigth - 1) and check_gate(set_of_boards[number], obstacle_coordinate_x, obstacle_coordinate_y - count):
                        set_of_boards[number][obstacle_coordinate_y - count][obstacle_coordinate_x] = obstacles[number]
                        numbers_of_obstacles -= 1
                    elif check_gate(set_of_boards[number], obstacle_coordinate_x, obstacle_coordinate_y + count):
                        set_of_boards[number][obstacle_coordinate_y + count][obstacle_coordinate_x] = obstacles[number]
                        numbers_of_obstacles -= 1
    return set_of_boards

def create_other_characters(set_of_boards, width=30, heigth=20):
    characters = ["🐻", "🐉", "👴"]
    obstacles = ["🌻", "🍄", "🔥"]
    items = ["🍞", "🪓", "🏹", "🌀", "🔰", "💍"]
    for number in range(len(set_of_boards)):
        for _ in range(6):
            character_coordinate_x = random.randint(1, width-2)
            character_coordinate_y = random.randint(1, heigth-2)
            if set_of_boards[number][character_coordinate_y][character_coordinate_x] not in obstacles and set_of_boards[number][character_coordinate_y][character_coordinate_x] not in items:
                set_of_boards[number][character_coordinate_y][character_coordinate_x] = characters[number]
            
            if number == len(set_of_boards)-1:
                break


def check_gate(board, coordinate_x, coordinate_y):
    if board[coordinate_y][coordinate_x + 1] == "🚪" or board[coordinate_y][coordinate_x - 1] == "🚪":
        return False
    return True


def put_player_on_board(board, player, old_coordinate):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    grounds = ["🟩", "🟫", "⬛"]
    board[old_coordinate[0]][old_coordinate[1]] = grounds[player["Player_position"][2]]
    board[player["Player_position"][0]][player["Player_position"][1]] = player["Player_icon"]
