from balanced_binary_search_tree import Tree
import random as rdn
#from chronometer import Chronometer

if __name__ == "__main__":
    tree_control = Tree()

    tree_control.insert_node([50,35,20,10,25,100,75,65,120,125,130,135,140])

    print('\nin order: ', end='')
    tree_control.in_order()
    print('\n')

    tree_control.check_balance()