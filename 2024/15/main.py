def read_board_fromfile(filename: str):
    board = []
    with open(filename, "r") as f:
        for line in f:
            board.append(list(line.strip()))
    return board


def read_moves_fromfile(filename: str):
    moves = []
    with open(filename, "r") as f:
        for line in f:
            moves.extend(list(line.strip()))
    return moves


def get_direction(d: str):
    if d == "^":
        return (-1, 0)
    elif d == "v":
        return (1, 0)
    elif d == "<":
        return (0, -1)
    elif d == ">":
        return (0, 1)
    return None


def is_valid(pos: (int, int)):
    return (
        pos is not None
        and pos[0] >= 0
        and pos[0] < len(board)
        and pos[1] >= 0
        and pos[1] < len(board[pos[0]])
    )


def get_char(pos: (int, int)):
    return board[pos[0]][pos[1]]


def is_wall(pos: (int, int)):
    return board[pos[0]][pos[1]] == "#"


def is_robot(pos: (int, int)):
    return board[pos[0]][pos[1]] == "@"


def is_empty(pos: (int, int)):
    return board[pos[0]][pos[1]] == "."


def is_box(pos: (int, int)):
    return any(
        (
            board[pos[0]][pos[1]] == "O",
            (board[pos[0]][pos[1]] == "[" and board[pos[0]][pos[1] + 1] == "]"),
            (board[pos[0]][pos[1]] == "]" and board[pos[0]][pos[1] - 1] == "["),
        )
    )


def can_push(pos: (int, int), d: str):
    # sokoban, recursive
    direction = get_direction(d)
    if direction is None:
        return False

    next_pos = (pos[0] + direction[0], pos[1] + direction[1])
    if is_wall(next_pos):
        return False

    if is_box(next_pos):
        # print("box", next_pos)
        can = can_push(next_pos, d)
        # print("can push", can)
        if can and (d == "^" or d == "v"):
            next_pos2 = None
            if get_char(next_pos) == "[":
                next_pos2 = (next_pos[0], next_pos[1] + 1)
            elif get_char(next_pos) == "]":
                next_pos2 = (next_pos[0], next_pos[1] - 1)
            if next_pos2 is not None:
                can = can and can_push(next_pos2, d)
        # print("can push box 2", can)
        return can

    return is_empty(next_pos)


def push(pos: (int, int), d: str):
    # sokoban, recursive
    direction = get_direction(d)
    if direction is None:
        return pos

    next_pos = (pos[0] + direction[0], pos[1] + direction[1])
    if is_box(next_pos):
        next_pos2 = None
        if d == "^" or d == "v":
            if get_char(next_pos) == "[":
                next_pos2 = (next_pos[0], next_pos[1] + 1)
            elif get_char(next_pos) == "]":
                next_pos2 = (next_pos[0], next_pos[1] - 1)

        push(next_pos, d)
        if next_pos2 is not None:
            # print("get pair of box", next_pos, next_pos2)
            push(next_pos2, d)

    if is_empty(next_pos):
        board[next_pos[0]][next_pos[1]] = board[pos[0]][pos[1]]
        board[pos[0]][pos[1]] = "."
        return next_pos

    return pos


def get_robot():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "@":
                return (i, j)
    return None


def print_board():
    for row in board:
        print("".join(row))
    print()


def get_coordinate_value(pos: (int, int)):
    return pos[0] * 100 + pos[1]


def get_board_value():
    ans = 0
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == "O" or cell == "[":
                ans += get_coordinate_value((i, j))
    return ans


def get_resized_chars(char: str):
    if char == "#":
        return ["#", "#"]
    if char == "O":
        return ["[", "]"]
    if char == "@":
        return ["@", "."]
    return [".", "."]


def resize_board(board):
    resized = []
    for row in board:
        tmp = []
        for char in row:
            tmp += get_resized_chars(char)
        resized.append(tmp)
    return resized


def part_one(board, moves):
    robot = get_robot()

    for d in moves:
        # print("Move", d)
        if can_push(robot, d):
            robot = push(robot, d)
        # print_board()

    return get_board_value()


def part_two(board, moves):
    robot = get_robot()

    for d in moves:
        # print("Move", d)
        if can_push(robot, d):
            # print("can push")
            robot = push(robot, d)
        # print_board()

    return get_board_value()


if __name__ == "__main__":
    SAMPLE = False

    board_filename = "input/board.sample.in" if SAMPLE else "input/board.star.in"
    moves_filename = "input/moves.sample.in" if SAMPLE else "input/moves.star.in"

    board = read_board_fromfile(board_filename)
    moves = read_moves_fromfile(moves_filename)

    print(part_one(board, moves))

    board = read_board_fromfile(board_filename)
    moves = read_moves_fromfile(moves_filename)

    board = resize_board(board)
    print(part_two(board, moves))
