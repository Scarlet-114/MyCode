
class Node:
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class BinaryTree:
    def __init__(self):
        self.root = None
        self.help_queue=[]

    def level_build_tree(self,node:Node):
        if not self.root:
            self.root = node
            self.help_queue.append(node)
        else:
            self.help_queue.append(node)
            if self.help_queue[0].lchild is None:
                self.help_queue[0].lchild = node
            else:
                self.help_queue[0].rchild = node
                self.help_queue.pop(0)

    def pre_order(self,curr_node:Node):
        if curr_node:
            print(curr_node.elem, end=' ')
            self.pre_order(curr_node.lchild)
            self.pre_order(curr_node.rchild)

    def level_order(self):
        help_queue = []
        help_queue.append(self.root)
        while help_queue:
            out_node = help_queue.pop(0)
            print(out_node.elem, end=' ')
            if out_node.lchild:
                help_queue.append(out_node.lchild)
            if out_node.rchild:
                help_queue.append(out_node.rchild)

if __name__ == '__main__':
    tree = BinaryTree()
    for i in range(1, 11):
        new_node = Node(i)
        tree.level_build_tree(new_node)
    tree.pre_order(tree.root)
    print()
    tree.level_order()