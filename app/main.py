from tree_node import TreeNode
import heapq
import copy
from puzzle import Puzzle
import time

easy = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
medium = [[0, 1, 2], [4, 5, 3], [7, 8, 6]]
hard = [[8, 7, 1], [6, 0, 2], [5, 4, 3]]

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def read_choice():
    while True:
        choice = input("Select your choice: ")
        try:
            return int(choice)
        except ValueError:
            print("Not a numerical value, try again.")


def in_bounds(x, y):
    return 0 <= x < 3 and 0 <= y < 3


def queueing_fn(node, nodes, algorithm):
    heuristic_val = 0
    node_puzzle = node.value
    zero_x = node_puzzle.get_zero_pos()[0]
    zero_y = node_puzzle.get_zero_pos()[1]

    # There are four direction we can move the 0 tile: up, down, left, and right
    for direction in directions:

        x = zero_x + direction[0]
        y = zero_y + direction[1]

        # Checks if swapping position is in-bounds
        if not in_bounds(x, y):
            continue

        queue_node_puzzle = copy.deepcopy(
            Puzzle(node_puzzle.get_puzzle(), node_puzzle.get_zero_pos()))
        queue_node_puzzle.swap_squares(x, y)

        if algorithm == "misplaced":
            heuristic_val = queue_node_puzzle.calculate_misplaced_tiles()
        elif algorithm == "manhattan":
            heuristic_val = queue_node_puzzle.calculate_manhattan_distance()

        heapq.heappush(
            nodes, TreeNode(queue_node_puzzle, heuristic_val, node.depth + 1))


def general_search(puzzle: Puzzle, algorithm: str):
    start = time.time()
    nodes = []
    max_queue_size = 0

    # Adding in the initial puzzle to the queue, taking into account of heuristics.
    if algorithm == "misplaced":
        heapq.heappush(nodes,
                       TreeNode(puzzle, puzzle.calculate_misplaced_tiles(), 0))
    elif algorithm == "manhattan":
        heapq.heappush(
            nodes, TreeNode(puzzle, puzzle.calculate_manhattan_distance(), 0))
    else:
        heapq.heappush(nodes, TreeNode(puzzle, 0, 0))
    num_nodes_expanded = 0
    repeats = []

    while not len(nodes) == 0:
        max_queue_size = max(max_queue_size, len(nodes))
        node = heapq.heappop(nodes)
        node_puzzle = node.value

        # If puzzle is repeated before, skip it.
        if node_puzzle.get_puzzle() in repeats:
            continue
        repeats.append(node_puzzle.get_puzzle())
        num_nodes_expanded += 1
        print(
            f"Best move where g(n) = {node.depth}, and h(n) = {node.heuristic}"
        )
        node_puzzle.print_puzzle()

        # Solved case
        if node_puzzle.is_solved():
            end = time.time()
            print("\nSolved with", algorithm, "algorithm")
            print("Num Nodes Expanded:", num_nodes_expanded)
            print("Max Heap Size:", max_queue_size)
            print("Depth Solution:", node.depth)
            print(f"Time: {round(end - start, 2)} seconds")
            node_puzzle.print_puzzle()
            return

        # If puzzle is not solved, then try queueing some puzzles.
        queueing_fn(node, nodes, algorithm)

    # If len(nodes) == 0 (meaning queue is empty), then the puzzle is unsolvable.
    print("\nUnsolvable")
    puzzle.print_puzzle()


def select_algorithm(puzzle: Puzzle):
    print("\nSelect Algorithm:")
    print("1. Uniform Search Cost")
    print("2. A* with the Misplaced Tile Heuristic")
    print("3. A* with the Manhattan Distance Heuristic")
    match read_choice():
        case 1:
            general_search(puzzle, "uniform")
        case 2:
            general_search(puzzle, "misplaced")
        case 3:
            general_search(puzzle, "manhattan")
        case _:
            return


def create_puzzle():
    zero_pos = [-1, -1]
    user_puzzle = []
    for i in range(3):
        numbers = ""
        while True:
            numbers = input(f"Type in 3 numbers for row {i}: ")
            numbers = numbers.split()
            if len(numbers) == 3:
                break
            print("Not 3 numbers! Try again.")

        numbers = [int(x) for x in numbers]

        if 0 in numbers:
            zero_pos = [i, numbers.index(0)]

        user_puzzle.append(numbers)

    return Puzzle(user_puzzle, zero_pos)


def main():

    print("Select Difficulty:")
    print("1. Easy (default)")
    print("2. Medium")
    print("3. Hard")
    print("4. Custom")
    print("5 <. Quit Program")

    match read_choice():
        case 1:
            puzzle = Puzzle(easy, [0, 2])
            select_algorithm(puzzle)
        case 2:
            puzzle = Puzzle(medium, [0, 0])
            select_algorithm(puzzle)
        case 3:
            puzzle = Puzzle(hard, [1, 1])
            select_algorithm(puzzle)
        case 4:
            puzzle = create_puzzle()
            select_algorithm(puzzle)
        case _:
            print("Quitting!")
            return


if __name__ == '__main__':
    main()
