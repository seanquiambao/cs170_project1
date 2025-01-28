class Puzzle:

    def __init__(self, puzzle, goal, zero_pos):
        self.puzzle = puzzle
        self.goal = goal
        self.zero_pos = zero_pos

    def get_puzzle(self):
        return self.puzzle

    def get_zero_pos(self):
        return self.zero_pos

    def set_zero_pos(self, new_pos):
        self.zero_pos = new_pos

    def is_solved(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.puzzle[i][j] != self.goal[i][j]:
                    return False
        return True

    def print_puzzle(self):
        for i in range(0, 3):
            print(self.puzzle[i])
        print("\n")

    def swap_squares(self, i, j):
        z_x = self.zero_pos[0]
        z_y = self.zero_pos[1]
        self.puzzle[z_x][z_y], self.puzzle[i][j] = self.puzzle[i][
            j], self.puzzle[z_x][z_y]
        self.set_zero_pos([i, j])
