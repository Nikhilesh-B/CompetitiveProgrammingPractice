
class TreeNode():
    def __init__(self, val, idx, children=[]):
        self.children = children
        self.val = val
        self.idx = idx



def compute_subtree_sums(root, sums):
    if not root.children:
        return root.val
    else:
        if root in sums:
            return sums[root]
        else:
            s = 0
            for child in root.children:
                s += compute_subtree_sums(child, sums)
            s+=root.val
            sums[]
            return s
                
        
        
               
        


def compute_new_tree(center, adj_matrix, data):
    root = TreeNode(val=data[center-1],idx=center)
    q = [root]
    explored = set(center)
    while q:
        node = q.pop()
        neighbors = adj_matrix[node.idx]
        children = []
        for n in neighbors:
            if n not in explored:
                new_child = TreeNode(val=data[n-1], idx=n)
                children.append(new_child)
                q.append(new_child)
    
        node.children = children
        explored.add(node.idx)
    return root        
       
        
def findCenter(edges, n, adj_matrix):
    #find the center of the tree as desired
    candidated_nodes = [i for i in range(1,n+1)]
    counts = dict()
    for e in edges:
        n_frm, n_to = e[0], e[1]
        
        if n_frm not in counts:
            counts[n_frm] = 1
        else:
            counts[n_frm] +=1 
        
        if n_to not in counts:
            counts[n_to] = 1
        else:
            counts[n_to] +=1 
    
    lf_nodes = set()
    for node in counts:
        if counts[node]==2:
            lf_nodes.add(node)
    
    explored = set()
    while len(candidated_nodes)>2:
        new_lf_nodes = set()
        for lf_node in lf_nodes:
            neighs = adj_matrix[lf_node]
            for n in neighs:
                if n not in explored:
                    explored.add(n)
                    new_lf_nodes.add(n)
        
        for lf_node in lf_nodes:
            candidated_nodes.remove(lf_node)
        
        lf_node = new_lf_nodes
        
    return candidated_nodes[0]

def compute_original_adj_matrix(edges):
    adj_matrix = dict()
    for e in edges:
        n_from, n_to = e[0], e[1]
        if n_from not in adj_matrix:
            adj_matrix[n_from] = [n_to]
        else:
            adj_matrix[n_from].append(n_to)
            
        n_from, n_to = n_to, n_from
        if n_from not in adj_matrix:
            adj_matrix[n_from] = [n_to]
        else:
            adj_matrix[n_from].append(n_to)
            
    return adj_matrix
        
def undirected(edges):
    new_edges = []
    
    for e in edges:
        new_edges.append([e[1],e[0]])
    
    return edges+new_edges
        


def cutTheTree(data, edges):
    n = len(data)
    copy_of_edge = edges.copy()
    undirected_edges = undirected(copy_of_edge)
    adj_matrix = compute_original_adj_matrix(edges)
    total_sum = sum(data)
    
    center = findCenter(undirected_edges, n, adj_matrix)
    root = compute_new_tree(center, adj_matrix, data)
    print(center)
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
