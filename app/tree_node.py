class TreeNode:

    order = 0

    def __init__(self, value, heuristic, depth):
        self.value = value
        self.heuristic = heuristic
        self.depth = depth
        TreeNode.order += 1

    def __lt__(self, other):
        fn_self = self.depth + self.heuristic
        fn_other = other.depth + other.heuristic

        if fn_self != fn_other:
            return fn_self < fn_other

        return self.order <= other.order
