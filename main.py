import util
import engine
import ui
import rouge_like_storymode
import random
import shutil

#terminal_middle
middle = shutil.get_terminal_size().columns

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOSS_START_X = 26
BOSS_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20

hall_of_fame = ["Péter", "Tamás", "Kristóf", "András", "Bálint"]

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

def place_boss(board):
    board[BOSS_START_Y][BOSS_START_X] = "🐉"
    board[BOSS_START_Y + 1][BOSS_START_X] = "🔥"
    board[BOSS_START_Y + 1][BOSS_START_X + 1] = "🔥"
    board[BOSS_START_Y + 1][BOSS_START_X - 1] = "🔥"
    board[BOSS_START_Y - 1][BOSS_START_X] = "🔥"
    board[BOSS_START_Y - 1][BOSS_START_X + 1] = "🔥"
    board[BOSS_START_Y - 1][BOSS_START_X - 1] = "🔥"
    board[BOSS_START_Y][BOSS_START_X + 1] = "🔥"
    board[BOSS_START_Y][BOSS_START_X - 1] = "🔥"
    board[BOSS_START_Y + 2][BOSS_START_X] = "🔥"
    board[BOSS_START_Y + 2][BOSS_START_X + 2] = "🔥"
    board[BOSS_START_Y + 2][BOSS_START_X - 2] = "🔥"
    board[BOSS_START_Y - 2][BOSS_START_X] = "🔥"
    board[BOSS_START_Y - 2][BOSS_START_X + 2] = "🔥"
    board[BOSS_START_Y - 2][BOSS_START_X - 2] = "🔥"
    board[BOSS_START_Y][BOSS_START_X + 2] = "🔥"
    board[BOSS_START_Y][BOSS_START_X - 2] = "🔥"
    board[BOSS_START_Y - 1][BOSS_START_X + 2] = "🔥"
    board[BOSS_START_Y - 1][BOSS_START_X - 2] = "🔥"
    board[BOSS_START_Y - 2][BOSS_START_X + 1] = "🔥"
    board[BOSS_START_Y - 2][BOSS_START_X - 1] = "🔥"
    board[BOSS_START_Y + 2][BOSS_START_X] = "🔥"
    board[BOSS_START_Y + 2][BOSS_START_X] = "🔥"
    board[BOSS_START_Y +2][BOSS_START_X+1] = "🔥"
    board[BOSS_START_Y-2][BOSS_START_X-1] = "🔥"
    board[BOSS_START_Y+1][BOSS_START_X+2] = "🔥"
    board[BOSS_START_Y-1][BOSS_START_X-2] = "🔥"
    board[BOSS_START_Y -2][BOSS_START_X+1] = "🔥"
    board[BOSS_START_Y +1][BOSS_START_X-2] = "🔥"
    board[BOSS_START_Y -2][BOSS_START_X-1] = "🔥"
    board[BOSS_START_Y +2][BOSS_START_X-1] = "🔥"




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
    enemies = ["🐻", "🐉", "👴", "🐲"]
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

def check_old_man(board, player):
    board_position = board[player["Player_position"][0]][player["Player_position"][1]]
    if board_position == "👴":
        rouge_like_storymode.oldman()
        player["Inventory"]["💍"] += 1


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


def main_game():
    util.clear_screen()
    #rouge_like_storymode.story()
    old_coordinate = [PLAYER_START_X, PLAYER_START_Y, 0]
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    util.clear_screen()
    is_running = True
    enemy_coordinates = get_enemy_coordinate(board)
    place_boss(board[3])
    while is_running:
        old_health = player["Health"]
        old_armor = player["Armor"]
        if check_movement(board[player["Player_position"][2]], player):
            check_door(player)
            check_old_man(board[player["Player_position"][2]], player)
            check_item(board[player["Player_position"][2]], player)
            engine.put_player_on_board(board[player["Player_position"][2]], player, old_coordinate, old_health, old_armor)
            engine.common_enemy_figth(player, board, enemy_coordinates[player["Player_position"][2]])
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
            if player["Player_position"][2] == 3:
                if board[3][player["Player_position"][0]][player["Player_position"][1]] == "🔥":
                    if player["Player_icon"] == "🧑" and player["Inventory"]["🪓"] == 3 and (player["Armor"] + player["Health"]) >= player["Max_health"]:
                        rouge_like_storymode.win()
                        hall_of_fame.append(player["Player_name"])
                        is_running = False
                    elif player["Player_icon"] == "🧝" and player["Inventory"]["🏹"] == 3 and (player["Armor"] + player["Health"]) >= player["Max_health"]:
                        rouge_like_storymode.win()
                        hall_of_fame.append(player["Player_name"])
                        is_running = False
                    elif player["Player_icon"] == "🧙" and player["Inventory"]["🌀"] == 3 and (player["Armor"] + player["Health"]) >= player["Max_health"]:
                        rouge_like_storymode.win()
                        hall_of_fame.append(player["Player_name"])
                        is_running = False
                    else:
                        is_running = False
                        rouge_like_storymode.dead()
        util.clear_screen()
        if player["Health"] == 0:
            is_running = False
            rouge_like_storymode.dead()

def hall():
    for i in range(len(hall_of_fame)):
        rouge_like_storymode.text_line(hall_of_fame[i])
    input()
    main()



def main():
    util.clear_screen()
    is_running2 = True
    while is_running2:
        util.clear_screen()
        print()
        print("*   Lord Of The PA     *".center(middle))
        print()
        print("[G]Play Game".center(middle))
        print("[H]Hall Of Fame".center(middle))
        print()
        print("[E]Exit]".center(middle))
        main_input = str(input())
        if main_input.upper() == "G":
            is_running2 = False
            main_game()
        if main_input.upper() == "H":
            hall()
            main()
        if main_input.upper() == "E":
            is_running2 = False
        else:
            KeyError("invalid input!")


if __name__ == '__main__':
    main()