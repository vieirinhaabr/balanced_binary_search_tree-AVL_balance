
<p align="center">
  <img width="200" height="200" style="align=center;" src="https://ssmic.com/UploadedFiles/images/transparent%20tree.png">
</p>

#### Project was made based on my classroom exercicies

<h1 style"align-text=center;"> Project: Balanced Binary Tree with AVL </h1>
 A project about Data Structure based on Tree Model with AVL Balance, different by <a href="https://github.com/wandreuscv/balanced_binary_search_tree">this tree</a>, AVL consists on a Tree with the same number of nodes in left and right, no by height. Confused? I will explain ...

## What I use?

I use Python and this libs:
    <ul>
      <li> drawtree (to print Tree) </li>
      <li> chronometer (to get time per instruction) </li>
      <li> random (to generate random numbers and insert they on tree) </li>
    </ul>

## How this project work?

I will explain step by step what this code do to balance the Tree:
  <ul>
    I will insert some nodes, in this example I will insert these how a list -> [1000,1500,700,500,300,100,550,350,150,750,725,775,800,850,770,875], ok lets do it.
    Different by the other balanced tree, in this case all Nodes will be inserted and only after this will be check the balance.
    <br>
	<li> After all Nodes inserted, Tree will looks how this: </li>
	<p align="center">
	<img src="https://i.ibb.co/Mn0RsZz/AVL-Balanced-Tree-Step-01.png" border="0">
	<p align="center">Ok, how I now the balance??</p>
	</p>
	<li>Is simple to understand, we will score to know if is balance, and if isn't what side is unbalanced:</li>
	<ul>
	<li>Since the end nodes have no subsequent nodes, start with the value 0</li>
	<li> A left node have +1 value (unitary)</li>
	<li> A right node have -1 value (unitary)</li>
	<li>Whatever if a node have right and left Node the result is 0 => Equilibrated</li>
	</ul>
	<li>Now you now how its made the check of balance (same how this code) we can check balance thogether:</li>
	<p align="center">
	<img src="https://i.ibb.co/B4tDwYX/AVL-Balanced-Tree-Step-02-1.png" border="0">
	<p align="center">How you can see, result in ''-3'', how is negative have more nodes on right side than left, need rotate to left (if result is positive, will be have more nodes on left).</p>
	</p>
	<li>Now we insert all Nodes and Tree is balanced, it will improve the search :D</li>
  </ul>
<br>

## About Functions

I will talk about some functions in the code above, what they do and how they work:
<br>

<h3 align="center">Node class</h3>
<h4 align="center">__init__</h4><p> Will start a new Node with Left side, Right side, and height empty </p> <h4 align="center">create_node</h4><p> Will insert a Node on Tree based on sequence, if is minor than root will be inserted on left side, if bigger will be inserted on right side, case the side is no empty, will be compare with next Node, same how root  </p>
<h3 align="center">Tree class</h3> <h4 align="center">__init__</h4><p> Will init the Tree with root empty (because the first insertion will be the root be default) </p> <h4 align="center">insert_node</h4><p> Will be check if is passing a list, a tuple or a interger, case its a list or tuple, it will be start a loop to insert the content ,insertion after insertion will be checked if is a interger, case not is a interger, it shows a error message and continue insertions calling **insert_in_tree** function</p> <h4 align="center">insert_in_tree</h4><p> Will be check if root is empty, case is empty, the first Node inserted will be the root, case isnt, will be inserted on Tree calling  **create_node** function on Node class, after this will be check if Tree need balance, calling **need_balance** function</p> <h4 align="center">in_order</h4><p> Will print the Nodes inserted **in order**, that consists in print left side first, root and right side for last</p> <h4 align="center">in_order</h4><p> Will print the Nodes inserted **in order**, that consists in print left side first, root and right side for last</p> <h4 align="center">print_tree</h4><p> Will print the Tree(using drawtree Lib) if this no have more than 500 Nodes</p> <h4 align="center">need_balance</h4><p> Will check if Tree need balance, case yes, him check where is highest and need rotation, after this him will call **rotate_right** or **rotate_left** to balance and after will call himself to check if need another rotation, case not, will be print a message</p> <h4 align="center">rotate_right</h4><p> Will be pass a Node from left side to right side to balance Tree if left Node of root havent right Node, case not, will be call **complex_rotate_right**</p> <h4 align="center">complex_rotate_right</h4><p> Is called case left Node of root have right Node, on this case, last Node from right side of left Node, of root will be passed to right side </p> <h4 align="center">rotate_left</h4><p> Will be pass a Node from right side to left side to balance Tree if right Node of root havent left Node, case not, will be call **complex_rotate_left**</p> <h4 align="center">complex_rotate_left</h4><p> Is called case right Node of root have left Node, on this case, last Node from left side of right Node, of root will be passed to left side </p> <h4 align="center">search_node</h4><p> Will search for a Node on Tree, if find will be return a success message, case not, will be show a failure message </p> <h4 align="center">print_tree_on_tuple</h4><p> Will print Tree on tuple form, how this way: 
Imagine, a Tuple how this (35, (20, (10, False, False), False), (50, False, False)), how you can see have a tuple inside other tuple, inside other, etc. Its because its created in this form, one tuple have (Info, Left Side, Right Side), if Left side is empty, it cotent a boolean False, if isnt, it will contain other tuple with Left content, its way have a tuple inside tuple :q, below you can see some images to facilitate your knowledge about this function, I will explain base on this Tuple "(35, (20, (10, False, False), False), (50, False, False))":</p>
<p align="center">
<img width="475" height="390" style="align=center;" src="https://i.ibb.co/WDg1bFm/Balanced-Tree-Tuple-Form.png">
</p>
<p></p>

## What a Balanced Binary Tree have different compared to a Simple Binary Tree?

<p align="center">
<img width="270" height="175" style="align=center;" src="https://i1.wp.com/www.techiedelight.com/wp-content/uploads/Height-Balanced-Tree-2.png?zoom=2.625&resize=368%2C275&ssl=1">
</p>

<p align="left">
  A Balanced Tree can improve a search on Tree making it more faster with some rules:
    <ul>
      <li> Left side and right side of the Tree need to have same height or in maximum one Node of difference in height (height its referenced by root of the Tree)</li>
      <li> If some side is more high, is doing a balance of Tree </li>
      <li> This model of balance involve passing Nodes from highest side to the lowest side (right or left) up until they have a maximum of one Node of height of difference or equal (You can see this on example image above)</li>
    </ul>
</p>
<br>
<p align="left">
  A Binary Tree without Balance which contain much insertions can spend so much time on a search, while a Balanced Tree can do it so much faster when have same height on sides
</p>
