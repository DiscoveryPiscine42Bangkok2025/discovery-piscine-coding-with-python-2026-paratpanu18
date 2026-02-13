#!/usr/bin/python3

from checkmate import checkmate

def display_board(board: str) -> None:
    rows = board.splitlines()
    for r in rows:
        print(" ".join(r))
    print("-" * 30)


def execute_case(title: str, board: str) -> None:
    print(f"[TEST] {title}")
    display_board(board)
    checkmate(board)
    print()


def main():

    test_cases = [
        # (description, board_string)

        ("Pawn attacks King (Success)", """\
R...
.K..
..P.
...."""),

        ("No piece attacks King (Fail)", """\
R...
.K..
....
...."""),

        ("Multiple Kings (Error)", """\
K...
....
...K
...."""),

        ("Invalid Character (Error)", """\
R...
.K..
..X.
...."""),

        ("Not Square Board (Error)", """\
R....
.K..
..P.
...."""),

        ("No King (Error)", """\
R...
....
....
...."""),

        ("Rook attacks King vertically (Success)", """\
.R..
.K..
R...
...."""),

        ("Rook attacks King horizontally (Success)", """\
....
.K.R
....
...."""),

        ("Bishop attacks King (Success)", """\
B...
.K..
....
...."""),

        ("Queen attacks King diagonally (Success)", """\
Q...
.K..
....
...."""),

        ("Queen attacks King horizontally (Success)", """\
..QK
....
....
...."""),

        ("Pawn at top edge (Fail)", """\
..P.
.K..
....
...."""),

        ("King attacked (Success)", """\
....
.RK.
.B..
...."""),

        ("Space normalization (Success)", """\
R...
 K..
  P.
....
"""),

        ("Single King only 1x1 (Fail)", "K"),
    ]

    for name, board in test_cases:
        execute_case(name, board)


if __name__ == "__main__":
    main()