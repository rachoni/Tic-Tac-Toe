import os
from game_logic.game import obtain_valid_position, play_turn, position_mapper, print_board
from stats.stats import show_stats
from stats.draw_stats import show_stats_draw


def save_game_result(winner_name):
    result_file_path = "data/result.txt"

    if not os.path.exists(result_file_path):
        with open(result_file_path, "w") as file:
            file.write(f"{winner_name}, 1\n")
        return

    with open(result_file_path, "r") as file:
        lines = file.readlines()

    content = ""
    is_new = True
    for line in lines:
        p_name, score = line.strip().split(', ')
        if p_name == winner_name:
            score = str(int(score) + 1)
            is_new = False
        content += f"{p_name}, {score}\n"

    if is_new:
        content += f"{winner_name}, 1\n"

    with open(result_file_path, "w") as file:
        file.write(content)


def play():
    player_one = input("Player 1 enter your name: ")
    player_two = input("Player 2 enter your name: ")

    while True:
        symbol = input(f"{player_one} select your symbol - either X or O: ").upper()
        if symbol in ["X", "O"]:
            break

    player_one_symbol = symbol
    player_two_symbol = "O" if player_one_symbol == "X" else "X"

    position_matrix = [list(range(i, i + 3)) for i in range(1, 10, 3)]
    print_board(position_matrix)

    print(f"{player_one} starts first")

    matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    player_to_symbol = {player_one: player_one_symbol, player_two: player_two_symbol}
    turns_count = 1

    while turns_count <= 9:
        current_player_name = player_one if turns_count % 2 == 1 else player_two
        position = obtain_valid_position(current_player_name, matrix)
        row, col = position_mapper[position]
        player_symbol = player_to_symbol[current_player_name]

        winner = play_turn(player_symbol, row, col, matrix, turns_count)
        if winner:
            print_board(matrix)
            print(f"{current_player_name} is the winner!")
            save_game_result(current_player_name)
            break

        turns_count += 1

        if turns_count == 10:
            print_board(matrix)
            print("Game over without winner")
            break


def main():
    command = input("Please select between: stats, stats_draw, play and end: ").lower()

    while True:
        if command == "stats":
            show_stats()
            break
        elif command == "stats_draw":
            show_stats_draw()
            break
        elif command == "play":
            play()
            break
        elif command == "end":
            exit(0)
        else:
            print("Invalid command, please try again.")
            command = input("Please select between: stats, stats_draw, play and end: ").lower()


if __name__ == "__main__":
    main()