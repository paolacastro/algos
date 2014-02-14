

class Node(object):
    def __init__(self, node):
        self.left = None
        self.right = None
        self.data = node


class BinaryTree(object):
    def __init__(self, array):
        self.array = array

    def build_tree(self, lo, hi):
        if lo > hi:
            return None

        else:
            mid = lo + (hi - lo) / 2
            node = Node(self.array[mid])
            left = self.build_tree(lo, mid - 1)
            right = self.build_tree(mid + 1, hi)
            node.left = left
            node.right = right
            print node.data
            return node

if __name__ == '__main__':
    use_these = [1, 2, 3, 6, 10, 11, 12]
    bt_obj = BinaryTree(use_these)
    lo = 0
    hi = len(use_these) - 1
    bt_obj.build_tree(lo, hi)
