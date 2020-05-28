import numpy as np
import json
import argparse
from tree import Tree, TreeNode
from inference import sum_product


def build_tree(data: dict) -> Tree:
    """This function generates a Tree object from a data dict.
    
    Arguments:
        data {dict} -- A dict obtained by parsing a json problem file.
    
    Returns:
        Tree -- A Tree object.
    DO NOT MODIFY THIS FUNCTION.
    """      
    nodes = dict()
    N = len(data['nodes'])
    # Intialize all the nodes.
    for i in range(N):
        __n = data['nodes'][str(i)]
        nodes[i] = TreeNode(i, __n['dim'])
    # Initialize a tree.
    tree = Tree(nodes)
    # Set the prior p(x0) for the tree.
    tree.p_0 = np.array(data['p_0'])
    # Connect the nodes and set the factors.
    for fr, v in data['factors'].items():
        for to, factor in v.items():
            nodes[int(fr)].children.append(nodes[int(to)])
            nodes[int(to)].parent = nodes[int(fr)]
            tree.factors[f'{fr}-{to}'] = np.array(factor)
    return tree

def test(tree: Tree, data: dict) -> str:
    """Tests the output marginals obtained from the sum_product function
       by comparing it against the correct marginals, i.e., data['marginals].
    
    Arguments:
        tree {Tree} -- A Tree object.
        data {dict} -- A dict obtained by parsing a json problem file.
    DO NOT MODIFY THIS FUNCTION.
    """    
    marginals = sum_product(tree, data['observations'])
    result = ''
    for k, v in marginals.items():
        expected = np.array(data['marginals'][str(k)])
        if np.allclose(v, expected):
            result += 'T'
        else: result += 'F'
    correct = result.count('T')
    print(f'{correct} of {len(result)} marginals correct.')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('problems',\
            type=str, nargs='+', help='path(s) to problem json files')
    args = parser.parse_args()
    for prob in args.problems:
        with open(prob, 'r') as fp:
            data = json.load(fp)
        tree = build_tree(data)
        test(tree, data)
