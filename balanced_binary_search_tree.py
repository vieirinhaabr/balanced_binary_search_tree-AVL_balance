#from drawtree import draw_bst

class Node(object):
    def __init__(self, info):
        self.info = info
        self.left_node = None
        self.right_node = None
        print("Node Inserted")

    def create_node(self, info):
        if info > self.info:
            if self.right_node is None:
                self.right_node = Node(info)
            else:
                self.right_node.create_node(info)
        elif info < self.info:
            if self.left_node is None:
                self.left_node = Node(info)
            else:
                self.left_node.create_node(info)
        else:
            print('Node ', info, ' is already on tree')


class Tree(object):
    def __init__(self):
        self.root = None
        self.elements_count = 0

    def insert_node(self, info):
        if type(info) == int:
            self.insert_in_tree(info)
        elif type(info) == list:
            for item in info:
                if type(item) == int:
                    self.insert_in_tree(item)
                else:
                    print('Int expected, but the item ', item, ' on List is ', type(item), ' type variable')
        elif type(info) == tuple:
            for item in info:
                if type(item) == int:
                    self.insert_in_tree(item)
                else:
                    print('Int expected, but the item ', item, ' on Tuple is ', type(item), ' type variable')
        else:
            print('Int or List expected, but ', info, ' is ', type(info), ' type variable')

    def insert_in_tree(self, info):
        if self.root is not None:
            self.root.create_node(info)
        else:
            self.root = Node(info)

    def in_order(self):
        self.in_order_run(self.root)

    def in_order_run(self, node):
        if node is None:
            return

        self.in_order_run(node.left_node)
        print(node.info, ' ', end='')
        self.in_order_run(node.right_node)

    def check_balance(self):
        return self.check_balance_run(self.root, list[0, 0])

    def check_balance_run(self, node, control_list):
        if (node.right_node is not None) and (node.left_node is not None):
            if node.info == self.root.info:
                self.check_balance_run(node.left_node)
                self.check_balance_run(node.right_node)
                return control_list
            else:

        elif node.right_node is not None:
            control_list[1] = control_list[1] + 1
            self.check_balance_run(node.right_node)
        elif node.left_node is not None:
            return 1 + self.check_balance_run(node.left_node)
        else:
            return 1