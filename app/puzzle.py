class Puzzle:
    # Goal states, and its positions for each value.
    # (The index of goal_pos are the tile's numbers), making manhattan distance
    # ...calculation more efficient
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    goal_pos = [[0, 0], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0],
                [2, 1], [2, 2]]

    def __init__(self, puzzle, zero_pos):
        self.puzzle = puzzle
        self.zero_pos = zero_pos

    # All the necessary getters and setters
    def get_puzzle(self):
        return self.puzzle

    def get_zero_pos(self):
        return self.zero_pos

    def set_zero_pos(self, new_pos):
        self.zero_pos = new_pos

    # Checks if puzzle is solved
    def is_solved(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.puzzle[i][j] != self.goal[i][j]:
                    return False
        return True

    # Prints the puzzle
    def print_puzzle(self):
        for i in range(0, 3):
            print(self.puzzle[i])
        print("\n")

    # Swaps the squares based on the i-th and j-th position
    def swap_squares(self, i, j):
        z_x = self.zero_pos[0]
        z_y = self.zero_pos[1]
        self.puzzle[z_x][z_y], self.puzzle[i][j] = self.puzzle[i][
            j], self.puzzle[z_x][z_y]
        self.set_zero_pos([i, j])

    # Calculates number of misplaced tiles, excluding the 0 tile
    def calculate_misplaced_tiles(self):
        count = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if self.puzzle[i][j] == 0:
                    continue
                if self.puzzle[i][j] != self.goal[i][j]:
                    count += 1

        return count

    # Calculates heuristic using the manhattan distance formula, excluding 0 tile.
    def calculate_manhattan_distance(self):
        manhattan_sum = 0
        for i in range(0, 3):
            for j in range(0, 3):
                val = self.puzzle[i][j]
                if val == 0:
                    continue

                manhattan_sum += abs(i - self.goal_pos[val][0]) + abs(
                    j - self.goal_pos[val][1])
        return manhattan_sum
