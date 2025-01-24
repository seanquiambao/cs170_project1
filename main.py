easy = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
medium = [[0, 1, 2], [4, 5, 3], [7, 8, 6]]
hard = [[8, 7, 1], [6, 0, 2], [5, 4, 3]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def print_puzzle(puzzle):
    for i in range(0, 3):
        print(puzzle[i])


def read_choice():
    while True:
        choice = input("Select your choice: ")
        try:
            return int(choice)
        except ValueError:
            print("Not a numerical value, try again.")


def uniform_search(puzzle):
    print_puzzle(puzzle)


def select_algorithm(puzzle):
    print("Select Algorithm:")
    print("1. Uniform Search Cost")
    print("2. A* with the Misplaced Tile Heuristic")
    print("3. A* with the Manhattan Distance Heuristic")
    match read_choice():
        case 1:
            uniform_search(puzzle)
        case _:
            return


def main():

    print("Select Difficulty:")
    print("1. Easy (default)")
    print("2. Medium")
    print("3. Hard")
    print("4 <. Quit Program")

    match read_choice():
        case 1:
            select_algorithm(easy)
        case 2:
            select_algorithm(medium)
        case 3:
            select_algorithm(hard)
        case _:
            print("Quitting!")
            return


if __name__ == '__main__':
    main()
