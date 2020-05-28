class TreeNode:
    """A class representing a variable node in the Bayesian Network.
    """    
    def __init__(self, node_id, dim, parent=None):
        """
        Arguments:
            node_id {int} -- A unique integer value.
            dim {int} -- The dimension of the discrete random variable
                         represented by this node.
        
        Keyword Arguments:
            parent {TreeNode} -- The parent node of this node. None for the root.
            (default: {None:TreeNode})
        """        
        self.parent = parent
        self.children = [] # A list of all the children of this node.
        self.id = node_id
        self.dim = dim
    def __str__(self):
        return f'(id={self.id}, dim={self.dim})'
    def __repr__(self):
        return f'(id={self.id}, dim={self.dim})'

class Tree:
    """A class representing a tree Bayesian Network.
    """
    def __init__(self, nodes):
        """
        Arguments:
            nodes {dict} -- A dict of the nodes in this tree. The keys of the
                            dict are node ids and the values are TreeNode objects.
        """        
        # The root node.
        self.root = nodes[0]

        # The prior distribution of the root node, i.e., p(x0).
        # This will hold a numpy array of shape (1, dim) where dim is the
        # dimension of the discrete distribution represented by p(x0).
        self.p_0 = None

        # A dict of all the nodes in this tree.
        self.nodes = nodes 

        # A dict for caching messages.
        self.messages = {} 

        # A dict of all the factors in this tree.
        # The keys of this dict are strings of the form 'from-to', where
        # from and to are node ids, and the values are numpy arrays of the
        # shape (from_dim, to_dim) where from_dim and to_dim are the dimensions
        # of the discrete distributions represented by the from and to nodes
        # respectively.
        # The factor values hold conditional probability tables (CPTs).
        # For example, self.factors['0-1'] will hold the p(x1 | x0) CPT.
        self.factors = {} 

        # A dict to hold unary or self factors.
        self.self_factors = {}
