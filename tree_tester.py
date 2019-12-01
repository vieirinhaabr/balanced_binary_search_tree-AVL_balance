from balanced_binary_search_tree import Tree
import random as rdn
from chronometer import Chronometer

if __name__ == "__main__":
    tree_control = Tree()

    #tree_control.insert_node([1000,50,1500,1502,1504,1506,1600,1550,1545,1548,1501,1503,1505,1450,1451,1400,1390,1401,1402,1403,1404,1405])

    with Chronometer() as t:
        tree_control.insert_node([1000,1500,700,500,300,100,550,350,150,750,725,775,800,850,770,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890])
    print('\n\nTo insert spend {:.5f} seconds'.format(float(t)))

    with Chronometer() as t:
        tree_control.print_tree()
    print('\nWas spend {:.5f} seconds in this operation'.format(float(t)))

    with Chronometer() as t:
        print('\nTrying to find 890 ...')
        tree_control.search_node(890)
    print('    Was spend {:.5f} seconds on this search before balance'.format(float(t)))
    print('\n')

    """"with Chronometer() as t:
        print('\nin order: ', end='')
        tree_control.transversal_order()
        print('\n')
    print('\n\nTo print !in order! spend {:.5f} seconds'.format(float(t)))"""

    with Chronometer() as t:
        tree_control.check_balance()
    print('\n\nTo print check balance {:.5f} seconds'.format(float(t)))

    with Chronometer() as t:
        tree_control.print_tree()
    print('\nWas spend {:.5f} seconds in this operation'.format(float(t)))

    with Chronometer() as t:
        print('\nTrying to find 890 ...')
        tree_control.search_node(890)
    print('    Was spend {:.5f} seconds on this search before balance'.format(float(t)))
    print('\n')

    """"with Chronometer() as t:
        print('\nin order after balance: ', end='')
        tree_control.transversal_order()
        print('\n')
    print('\n\nTo print !in order! after balance spend {:.5f} seconds'.format(float(t)))"""

    with Chronometer() as t:
        tree_control.check_balance()
    print('\n\nTo print check balance again {:.5f} seconds'.format(float(t)))

    with Chronometer() as t:
        tree_control.check_balance()
    print('\n\nTo print check balance again {:.5f} seconds'.format(float(t)))