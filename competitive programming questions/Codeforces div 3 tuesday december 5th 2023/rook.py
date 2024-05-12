COLS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ROWS = [1, 2, 3, 4, 5, 6, 7, 8]


def process_square(square):
    column = square[0]
    row = int(square[1])
    potential_squares = {column+str(r) for r in ROWS} | {col+str(row) for col in COLS}
    potential_squares.remove(square)
    for potential_square in potential_squares:
        print(potential_square)


if __name__ == "__main__":
    n_test_cases = int(input())
    squares = []
    while n_test_cases > 0:
        square = input()
        squares.append(square)
        n_test_cases -= 1

    for square in squares:
        process_square(square)
