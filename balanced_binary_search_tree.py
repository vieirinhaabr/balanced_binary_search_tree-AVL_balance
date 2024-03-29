from drawtree import draw_bst

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
    
    def transversal_order(self):
        self.transversal_order_order_run(self.root)

    def transversal_order_order_run(self, node):
        if node is None:
            return

        print(node.info, ' ', end='')
        self.transversal_order_order_run(node.left_node)
        self.transversal_order_order_run(node.right_node)

    def check_balance(self):
        if self.root is not None:
            check = self.verify_balance(self.root, [0, 0])
            balance = check[0] - check[1]
            print(balance, "\n")
            if balance > 1:
                print("\nNeed rotate to -> Right")
                balance = self.bst_root_right(balance)
                if balance > 1:
                    balance = self.bst_rotate_right(self.root.left_node, balance)
                    if balance > 1:
                        print("balance using right side")
                        balance = self.bst_rotate_right(self.root.right_node, balance)
                        if balance > 1:
                            print("Failure during balance !!!")
            elif balance < -1:
                print("\nNeed rotate to -> Left")
                balance = self.bst_root_left(balance)
                if balance < -1:
                    balance = self.bst_rotate_left(self.root.right_node, balance)
                    if balance < -1:
                        print("balance using left side")
                        balance = self.bst_rotate_left(self.root.left_node, balance)
                        if balance < -1:
                            print("Failure during balance !!!")

    def verify_balance(self, node, control_list):
        if (node.right_node is not None) or (node.left_node is not None):
            if (node.right_node is not None) and (node.left_node is not None):
                control_list[0] = control_list[0] + 1
                control_list[1] = control_list[1] + 1
                control_list = self.verify_balance(node.left_node, control_list)
                control_list = self.verify_balance(node.right_node, control_list)
                return control_list
            elif node.right_node is not None:
                control_list[1] = control_list[1] + 1
                control_list = self.verify_balance(node.right_node, control_list)
                return control_list
            else:
                control_list[0] = control_list[0] + 1
                control_list = self.verify_balance(node.left_node, control_list)
                return control_list
        else:
            return control_list

    def bst_root_left(self, balance):
        if self.root.right_node is not None:
            if self.root.right_node.left_node is None:
                temp = self.root
                self.root = self.root.right_node
                temp.right_node = None
                self.root.left_node = temp
                balance = balance + 2
                if balance < -1:
                    balance = self.bst_root_left(balance)
            if balance < -1:
                if self.root.right_node is not None:
                    if self.root.right_node.right_node is not None:
                        if self.root.right_node.right_node.left_node is None:
                            temp = self.root.right_node
                            self.root.right_node = self.root.right_node.right_node
                            temp.right_node = None
                            self.root.right_node.left_node = temp
                            balance = balance + 2
                            if balance < -1:
                                balance = self.bst_root_left(balance)
        if balance < -1:
            if self.root.left_node is not None:
                if self.root.left_node.right_node is not None:
                    if self.root.left_node.right_node.left_node is None:
                        temp = self.root.left_node
                        self.root.left_node = self.root.left_node.right_node
                        temp.right_node = None
                        self.root.left_node.left_node = temp
                        balance = balance + 2
                        if balance < -1:
                            balance = self.bst_root_left(balance)
        return balance

    def bst_rotate_left(self, node, balance):
        if node is None:
            return balance
        if node.right_node is not None:
            if node.right_node.right_node is not None:
                if node.right_node.right_node.left_node is None:
                    temp = node.right_node
                    node.right_node = node.right_node.right_node
                    temp.right_node = None
                    node.right_node.left_node = temp
                    balance = balance + 2
                    print(balance,'/n')
                    if balance < -1:
                        balance = self.bst_rotate_left(node, balance)
            if balance < -1:
                balance = self.bst_rotate_left(node.right_node, balance)
        if balance < -1:
            if node.left_node is not None:
                if node.left_node.right_node is not None:
                    if node.left_node.right_node.left_node is None:
                        temp = node.left_node
                        node.left_node = node.left_node.right_node
                        temp.right_node = None
                        node.left_node.left_node = temp
                        balance = balance + 2
                        if balance < -1:
                            balance = self.bst_rotate_left(node, balance)
                if balance < -1:
                    balance = self.bst_rotate_left(node.left_node, balance)
        return balance

    def bst_root_right(self, balance):
        if self.root.left_node is not None:
            if self.root.left_node.right_node is None:
                temp = self.root
                self.root = self.root.left_node
                temp.left_node = None
                self.root.right_node = temp
                balance = balance - 2
                if balance > 1:
                    balance = self.bst_root_right(balance)
            if balance > 1:
                if self.root.left_node is not None:
                    if self.root.left_node.left_node is not None:
                        if self.root.left_node.left_node.right_node is None:
                            temp = self.root.left_node
                            self.root.left_node = self.root.left_node.left_node
                            temp.left_node = None
                            self.root.left_node.right_node = temp
                            balance = balance - 2
                            if balance > 1:
                                balance = self.bst_root_right(balance)
        if balance > 1:
            if self.root.right_node is not None:
                if self.root.right_node.left_node is not None:
                    if self.root.right_node.left_node.right_node is None:
                        temp = self.root.right_node
                        self.root.right_node = self.root.right_node.left_node
                        temp.left_node = None
                        self.root.right_node.right_node = temp
                        balance = balance + 2
                        if balance > 1:
                            balance = self.bst_root_right(balance)
        return balance

    def bst_rotate_right(self, node, balance):
        if node is None:
            return balance
        if node.left_node is not None:
            if node.left_node.left_node is not None:
                if node.left_node.left_node.right_node is None:
                    temp = node.left_node
                    node.left_node = node.left_node.left_node
                    temp.left_node = None
                    node.left_node.right_node = temp
                    balance = balance - 2
                    if balance > 1:
                        balance = self.bst_rotate_right(node, balance)
            if balance > 1:
                balance = self.bst_rotate_right(node.right_node, balance)
        if balance > 1:
            if node.right_node is not None:
                if node.right_node.left_node is not None:
                    if node.right_node.left_node.right_node is None:
                        temp = node.right_node
                        node.right_node = node.right_node.left_node
                        temp.left_node = None
                        node.right_node.right_node = temp
                        balance = balance - 2
                        if balance > 1:
                            balance = self.bst_rotate_right(node, balance)
                if balance > 1:
                    balance = self.bst_rotate_right(node.left_node, balance)
        return balance

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