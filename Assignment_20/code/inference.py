# Matric Number: Add Your Matric Number Here.
# Please add comments to explain your logic, wherever necessary.

import numpy as np
from functools import reduce
from tree import Tree, TreeNode

def sum_product(tree: Tree, observations: dict) -> dict:
    """Implementation of the Sum-Product algorithm for directed trees.
    
    Arguments:
        tree {Tree} -- A Tree object.
        observations {dict} -- A dict of observations where keys are node ids
                               and values are the observed values of the nodes.
                               For example, {"0": 1, "2": 0} means nodes 0 and 2 
                               have the values 1 and 0 respectively.
    Returns:
        dict -- A dict of marginals for all the nodes. The keys of this dict are
                node ids and the values are numpy arrays of shape (1, dim) where 
                dim is the dimension of the node.
    """    
    setup_self_factors(tree, observations)
    root = tree.root
    for c in root.children:
        collect(tree, root, c)
    for c in root.children:
        distribute(tree, root, c)
    return compute_marginals(tree)

def setup_self_factors(tree: Tree, observations: dict) -> None:
    """This function sets up the self-factors for each node and assigns
       these values to tree.self_factors for each node.
    
    Arguments:
        tree {Tree} -- A Tree object.
        observations {dict} -- A dict of observations where keys are node ids
                               and values are the observed values of the nodes.
                               For example, {"0": 1, "2": 0} means nodes 0 and 2 
                               have the values 1 and 0 respectively.
    """
    # Your code goes here.
    pass

def collect(tree: Tree, to_node: TreeNode, from_node: TreeNode) -> None:
    """This function collects messages from child node to parent node.
    
    Arguments:
        tree {Tree} -- A Tree object.
        to_node {TreeNode} -- The parent node to which the message is sent.
        from_node {TreeNode} -- The child node from which the message is sent.
    """
    # Your code goes here.
    pass

def distribute(tree: Tree, from_node: TreeNode, to_node: TreeNode) -> None:
    """This function distributes messages from parent node to child node.
    
    Arguments:
        tree {Tree} -- A Tree object.
        from_node {TreeNode} -- The parent node from which the message is sent.
        to_node {TreeNode} -- The child node to which the message is sent.
    """
    # Your code goes here.
    pass

def send_message(tree: Tree, from_node: TreeNode, to_node: TreeNode) -> None:
    """This function sends a message from from_node to to_node. This function
       assumes that all the messages required to send a message from from_node
       to to_node have already been cached in tree.messages.

       Upon completion, this function doesn't return anything but caches the 
       message from from_node to to_node in tree.messages.
    
    Arguments:
        tree {Tree} -- A Tree object.
        from_node {TreeNode} -- A TreeNode object from which the message is
                                is being sent.
        to_node {TreeNode} -- A TreeNode object to which the message is
                                is being sent.
    """
    # Your code goes here.
    pass 

def compute_marginals(tree: Tree) -> dict:
    """This function computes the marginals of all nodes in the tree
       once all the messages have been cached in tree.messages.

       For example, for the following tree with all nodes representing
       binary random variables, this function will return: 
       {0: p(x0),
        1: p(x1),
        2: p(x2)}

                0 ----> 1
                |
                ------> 2

       For the following tree with all nodes representing
       a binary random variables and the observation {"3": 1}, this function
       will return:
       {0: p(x0 | x3 = 1),
        1: p(x1 | x3 = 1),
        2: p(x2 | x3 = 1),
        3: p(x3 | x3 = 1)}

                0 ----> 1 ----> 3
                |
                ------> 2

        Since x3 is observed in this case, p(x3 | x3 = 1) is equal to
        np.array([[0., 1.]]).
     
    Arguments:
        tree {Tree} -- A Tree object.
    
    Returns:
        dict -- A dict of marginals for all the nodes. The keys of this dict are
                node ids and the values are numpy arrays of shape (1, dim) where 
                dim is the dimension of the node.
    """
    # Your code goes here.
    pass 

