class TreeNode:

    # Tie-breaker variable
    order = 0

    def __init__(self, value, heuristic, depth):
        self.value = value
        self.heuristic = heuristic
        self.depth = depth
        TreeNode.order += 1

    # Used for A* algorithms to calculate f(n) = g(n) + h(n)
    # For a tie-breaker, we simply take the node that was pushed in first.
    # As far as I know, there is no weighted costs for moving the tiles
    # ...so the "cost" is essentially the depth.
    def __lt__(self, other):
        fn_self = self.depth + self.heuristic
        fn_other = other.depth + other.heuristic

        if fn_self != fn_other:
            return fn_self < fn_other

        return self.order <= other.order
