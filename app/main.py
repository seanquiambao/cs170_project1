from queue import Queue

from tree_node import TreeNode
import queue
import copy
from puzzle import Puzzle

easy = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
medium = [[0, 1, 2], [4, 5, 3], [7, 8, 6]]
hard = [[8, 7, 1], [6, 0, 2], [5, 4, 3]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

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


# queues all puzzle combination, basically swaps empty square in four different directions
def queueing_fn(node, nodes: Queue):

    zero_x = node.get_zero_pos()[0]
    zero_y = node.get_zero_pos()[1]

    for direction in directions:
        # for each direction, check if the swapping position is in bounds
        x = zero_x + direction[0]
        y = zero_y + direction[1]

        if in_bounds(x, y):
            # if it is, make a deep copy and push it to queue
            queue_node = copy.deepcopy(
                Puzzle(node.get_puzzle(), goal, [zero_x, zero_y]))
            queue_node.swap_squares(x, y)
            nodes.put(queue_node)


def uniform_cost_search(puzzle: Puzzle):
    puzzle.print_puzzle()


def a_star_missing_tiles(puzzle: Puzzle):
    puzzle.print_puzzle()


def a_star_manhattan_distance(puzzle: Puzzle):
    puzzle.print_puzzle()


def general_search(puzzle: Puzzle):
    nodes = queue.Queue()
    nodes.put(puzzle)
    num_nodes_expanded = 0
    repeats = []

    while not nodes.empty():
        node = nodes.get()
        if node.get_puzzle() in repeats:
            continue
        repeats.append(node.get_puzzle())
        num_nodes_expanded += 1

        if node.is_solved():
            print("Solved!")
            print("Number of nodes expanded:", num_nodes_expanded)
            node.print_puzzle()
            return
        queueing_fn(node, nodes)

    print("Unsolvable")
    return


def select_algorithm(puzzle: Puzzle):
    print("Select Algorithm:")
    print("1. General Search")
    print("2. Uniform Search Cost")
    print("3. A* with the Misplaced Tile Heuristic")
    print("4. A* with the Manhattan Distance Heuristic")
    match read_choice():
        case 1:
            general_search(puzzle)
        case 2:
            uniform_cost_search(puzzle)
        case 3:
            a_star_missing_tiles(puzzle)
        case 4:
            a_star_manhattan_distance(puzzle)
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
            puzzle = Puzzle(easy, goal, [0, 2])
            select_algorithm(puzzle)
        case 2:
            puzzle = Puzzle(medium, goal, [0, 0])
            select_algorithm(puzzle)
        case 3:
            puzzle = Puzzle(hard, goal, [1, 1])
            select_algorithm(puzzle)
        case _:
            print("Quitting!")
            return


if __name__ == '__main__':
    main()
