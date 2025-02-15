class InvalidPositionNumberError(Exception):
    pass


class PositionAlreadyTakenError(Exception):
    pass


def obtain_valid_position(player_name, mtrx):
    while True:
        try:
            selected_position = int(input(f"{player_name}, please select a spot: "))
            if selected_position < 1 or selected_position > 9:
                raise InvalidPositionNumberError
            r, c = position_mapper[selected_position]
            if mtrx[r][c] != " ":
                raise PositionAlreadyTakenError
            return selected_position
        except ValueError:
            print("Please enter a valid number")
        except InvalidPositionNumberError:
            print("Please enter a number between 1-9")
        except PositionAlreadyTakenError:
            print("Please select an empty position")


def print_board(mtrx):
    for r in mtrx:
        print(f"|  {'  |  '.join(r)}  |")


def is_winner(p_symbol, mtrx):
    matrix_length = len(mtrx)

    for r in mtrx:
        if all([el == p_symbol for el in r]):
            return True

    for c_idx in range(matrix_length):
        if all([mtrx[r_idx][c_idx] == p_symbol for r_idx in range(matrix_length)]):
            return True

    main_diagonal_winner = all([mtrx[index][index] == p_symbol for index in range(matrix_length)])
    opos_diagonal_winner = all([mtrx[matrix_length - 1 - c_idx][c_idx] == p_symbol for c_idx in range(matrix_length)])

    if main_diagonal_winner or opos_diagonal_winner:
        return True

    return False


def play_turn(p_symbol, r, c, mtrx, trns_cnt):
    mtrx[r][c] = p_symbol

    if trns_cnt > 4:
        return is_winner(p_symbol, mtrx)

    print_board(mtrx)
    return False


position_mapper = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2)
}