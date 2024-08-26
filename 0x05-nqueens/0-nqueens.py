#!/usr/bin/python3
"""sloving the N queen puzzle by placing N non attacking
queen on an NxN chessboard
"""
import sys


def solve_queen(size):
    """function to solve the placement of queen"""
    solutions = []  # Initialize solutions list
    # initialize queen to start from 0
    queen_placed = [0] * size
    # function to recursively find all solutions by starting from 0
    place_queen(solutions, queen_placed, 0, size)
    return solutions


def is_valid_position(queen_place, col):
    """Check if it's a valid position"""
    for i in range(col):
        # check if the queen is place in the same col
        if queen_place[i] == queen_place[col]:
            return False
        # check if the queen is place in the same diagonal
        if abs(queen_place[i] - queen_place[col]) == abs(i - col):
            return False
    return True


def place_queen(solutions, queen_placed, col, size):
    """ function to place the queen  """
    if col >= size:
        solutions.append(queen_placed[:])
        return
    for i in range(size):
        queen_placed[col] = i
        if is_valid_position(queen_placed, col):
            # recursion function
            place_queen(solutions, queen_placed, col + 1, size)


def main():
    """main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_queen(size)
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])


if __name__ == "__main__":
    main()
