from drawtree import draw_bst

class Node(object):
    def __init__(self, info):
        self.info = info
        self.left_node = None
        self.right_node = None
        self.left_height = 0
        self.right_height = 0
        print("Node Inserted")

    def create_node(self, info):
        if info > self.info:
            if self.right_node is None:
                self.right_node = Node(info)
                self.right_height = 1
                return 1
            else:
                height = self.right_node.create_node(info) + 1
                if height > self.right_height:
                    self.right_height = height
                return height
        elif info < self.info:
            if self.left_node is None:
                self.left_node = Node(info)
                self.left_height = 1
                return 1
            else:
                height = self.left_node.create_node(info) + 1
                if height > self.left_height:
                    self.left_height = height
                return height
        else:
            print('Node ', info, ' is already on tree')
            return 0


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
            self.need_balance(self.root)
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

    def print_tree(self):
        self.tree_list = []
        self.print_tree_run(self.root)

        if len(self.tree_list) > 500:
            print("Tree have more than 500 Elements, wasn't possible to print")
        else:
            draw_bst(self.tree_list)

    def print_tree_run(self, node):
        if node is None:
            return

        self.tree_list.append(node.info)
        self.print_tree_run(node.left_node)
        self.print_tree_run(node.right_node)

    def need_balance(self, node):
        counter = node.left_height - node.right_height
        if counter > 1:
            #rotate to right
            print('rotate to right: counter -> ', counter)
            self.rotate_right(self.root)
            self.need_balance(self.root)
        elif counter < -1:
            #rotate to left
            print('rotate to left: counter -> ', counter)
            self.rotate_left(self.root)
            self.need_balance(self.root)
        else:
            print("Don't need balance !!!\n")

    def rotate_right(self, node):
        if node.left_node is not None:
            if node.left_node.right_node is None:
                self.root = self.root.left_node
                self.root.right_node = node
                self.root.right_height = node.right_height + 1
                node.left_height = 0
                node.left_node = None
                print('Concluded: Simple-Rotate to right.\n')
            else:
                if node.left_node.left_height < node.left_node.right_height:
                    self.complex_rotate_right(node.left_node, True)
                else:
                    self.complex_rotate_right(node.left_node, False)
        else:
            print('Failure during rotation: No node detected to rotate!')

    def complex_rotate_right(self, node, isLong):
        if node.right_node.right_node is not None:
            node.right_height = node.right_height - 1
            self.complex_rotate_right(node.right_node, isLong)
        else:
            node.right_height = node.right_height - 1
            s = node.right_node
            if node.right_node.left_node is not None:
                node.right_node = node.right_node.left_node
            else:
                node.right_node = None
            f = self.root
            self.root = s
            self.root.left_node = f.left_node
            self.root.right_node = f

            if isLong:
                self.root.left_height = f.left_height - 1
            else:
                self.root.left_height = f.left_height

            self.root.right_height = f.right_height + 1
            self.root.right_node.left_height = 0
            self.root.right_node.left_node = None
            print('Concluded: Complex-Rotate to right.\n')

    def rotate_left(self, node):
        if node.right_node is not None:
            if node.right_node.left_node is None:
                self.root = self.root.right_node
                self.root.left_node = node
                self.root.left_height = node.left_height + 1
                node.right_height = 0
                node.right_node = None
                print('Concluded: Simple-Rotate to left.\n')
            else:
                if node.right_node.right_height < node.right_node.left_height:
                    self.complex_rotate_left(node.right_node, True)
                else:
                    self.complex_rotate_left(node.right_node, False)
        else:
            print('Failure during rotation: No node detected to rotate!')

    def complex_rotate_left(self, node, isLong):
        if node.left_node.left_node is not None:
            node.left_height = node.left_height - 1
            self.complex_rotate_left(node.left_node, isLong)
        else:
            node.left_height = node.left_height - 1
            s = node.left_node
            if node.left_node.right_node is not None:
                node.left_node = node.left_node.right_node
            else:
                node.left_node = None
            f = self.root
            self.root = s
            self.root.right_node = f.right_node
            self.root.left_node = f

            if isLong:
                self.root.right_height = f.right_height - 1
            else:
                self.root.right_height = f.right_height

            self.root.left_height = f.left_height + 1
            self.root.left_node.right_height = 0
            self.root.left_node.right_node = None
            print('Concluded: Complex-Rotate to right.\n')

    def search_node(self, search):
        calls = self.search_node_run(self.root, search) + 1
        print('    Was made ', calls, ' calls on this operation!')

    def search_node_run(self, node, search):
        if node is not None:
            if node.info == search:
                print('    Node ', node.info, ' find!!!')
                return 0
            elif node.info < search:
                return 1 + self.search_node_run(node.right_node, search)
            else:
                return 1 + self.search_node_run(node.left_node, search)
        else:
            print('\n    Node is no present on Tree!!')
            return 0

    def print_tree_on_tuple(self):
        if self.root is None:
            print("    Wasn't find a Node on Tree")
        else:
            tuple_tree = self.create_tree_tuple(self.root)

            return tuple_tree

    def create_tree_tuple(self, node):
        if (node.left_node is None) and (node.right_node is None):
            return (node.info, False, False)
        elif node.right_node is None:
            return (node.info, self.create_tree_tuple(node.left_node), False)
        elif node.left_node is None:
            return (node.info, False, self.create_tree_tuple(node.right_node))
        else:
            return (node.info, self.create_tree_tuple(node.left_node), self.create_tree_tuple(node.right_node))