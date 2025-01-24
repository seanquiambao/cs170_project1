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
        if choice.isdigit():
            return int(choice)
        print("Not a numerical value, try again.")


def main():

    print("Select Difficulty:")
    print("1. Easy (default)")
    print("2. Medium")
    print("3. Hard")
    print("4 <. Quit Program")

    match read_choice():
        case 1:
            print("HI?")
            print_puzzle(easy)
        case 2:
            print_puzzle(medium)
        case 3:
            print_puzzle(hard)
        case _:
            print("Quitting!")
            return


if __name__ == '__main__':
    main()
