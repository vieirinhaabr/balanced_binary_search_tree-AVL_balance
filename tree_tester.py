from balanced_binary_search_tree import Tree
import random as rdn
#from chronometer import Chronometer

if __name__ == "__main__":
    tree_control = Tree()

    tree_control.insert_node([1000,50,1500,1502,1504,1506,1600,1550,1545,1548,1501,1503,1505,1450,1451,1400,1390,1401,1402,1403,1404,1405])

    print('\nin order: ', end='')
    tree_control.in_order()
    print('\n')

    tree_control.check_balance()

    print('\nin order after balance: ', end='')
    tree_control.in_order()
    print('\n')