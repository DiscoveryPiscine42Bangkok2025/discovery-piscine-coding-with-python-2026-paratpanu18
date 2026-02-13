def get_board_size(board: str) -> int | None:
    lines = board.splitlines()
    size = len(lines)

    if size == 0:
        print("Error: empty board")
        return None

    if not all(len(line) == size for line in lines):
        print("Error: board must be square")
        return None

    return size


def sanitize_board(board: str) -> str | None:
    if board is None:
        return None
    return board.replace(" ", ".")


def is_valid_symbol(symbol: str) -> bool:
    allowed = {'K', 'Q', 'R', 'B', 'P', '.'}
    return symbol in allowed


def validate_board_content(board: str, size: int) -> bool:
    lines = board.splitlines()
    kings = 0

    for line in lines:
        if len(line) != size:
            return False

        for cell in line:
            if not is_valid_symbol(cell):
                print("Error: invalid piece")
                return False
            if cell == 'K':
                kings += 1

    if kings != 1:
        print("Error: there must be exactly one king")
        return False

    return True


def to_matrix(board: str) -> list[list[str]]:
    return [list(row) for row in board.splitlines()]


def find_king_position(matrix: list[list[str]]) -> tuple[int, int]:
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 'K':
                return i, j


def inside(r: int, c: int, size: int) -> bool:
    return 0 <= r < size and 0 <= c < size


def pawn_attacks(r: int, c: int, king_pos: tuple[int, int], size: int) -> bool:
    directions = [(-1, -1), (-1, 1)]

    return any(
        inside(r + dr, c + dc, size) and (r + dr, c + dc) == king_pos
        for dr, dc in directions
    )


def attack_with_directions(
    matrix: list[list[str]],
    r: int,
    c: int,
    king_pos: tuple[int, int],
    vectors: list[tuple[int, int]]
) -> bool:

    size = len(matrix)

    for dr, dc in vectors:
        nr, nc = r + dr, c + dc

        while inside(nr, nc, size):
            if (nr, nc) == king_pos:
                return True

            if matrix[nr][nc] != '.':
                break

            nr += dr
            nc += dc

    return False


def checkmate(board: str) -> None:
    board = sanitize_board(board)
    if board is None:
        print("Error: board is None")
        return

    size = get_board_size(board)
    if size is None:
        return

    if not validate_board_content(board, size):
        return

    matrix = to_matrix(board)
    king_pos = find_king_position(matrix)

    attack_patterns = {
        'R': [(1,0), (-1,0), (0,1), (0,-1)],
        'B': [(1,1), (1,-1), (-1,1), (-1,-1)],
        'Q': [(1,0), (-1,0), (0,1), (0,-1),
              (1,1), (1,-1), (-1,1), (-1,-1)]
    }

    for r in range(size):
        for c in range(size):
            piece = matrix[r][c]

            if piece in {'.', 'K'}:
                continue

            elif piece == 'P' and pawn_attacks(r, c, king_pos, size):
                print("Success")
                return

            elif piece in attack_patterns and attack_with_directions( # R, B, Q
                matrix, r, c, king_pos, attack_patterns[piece]
            ):
                print("Success")
                return

    print("Fail")