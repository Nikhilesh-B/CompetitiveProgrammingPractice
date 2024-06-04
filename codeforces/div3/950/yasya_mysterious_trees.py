def XOR_all_edges(x, edge_dict):
    for edge in edge_dict:
        edge_dict[edge] = edge_dict[edge] ^ x

def dfs_max_cycle_XOR(node, weight, adj_list):
    max_cycle_xor = -1
    visited = set()
    stack = [node]
    running_XORs = {node: weight}
    while stack: 
        u = stack.pop()
        visited.add(u)
        for v, edge_w in adj_list[u]:
            if v not in visited:
                stack.append(v)
                running_XOR = running_XORs[u] ^ edge_w
                running_XORs[v] = running_XOR
                max_cycle_xor = max(max_cycle_xor, running_XOR)

    return max_cycle_xor

def print_max_cycle_XOR(node, weight, edge_dict):
    adj_list = {}
    for edge in edge_dict:
        u, v = edge
        if u not in adj_list:
            adj_list[u] = []
        if v not in adj_list:
            adj_list[v] = []
        adj_list[u].append((v, edge_dict[edge]))
        adj_list[v].append((u, edge_dict[edge]))
    
    max_cycle_XOR = dfs_max_cycle_XOR(node, weight, adj_list)
    print(max_cycle_XOR, end=" ")

def process_case(n, m, edge_dict, query_set):
    for qidx in range(m):
        query = query_set[qidx]
        if query[0] == "^":
            x = query[1]
            XOR_all_edges(x, edge_dict)
        else:
            node = query[1]
            weight = query[2]
            print_max_cycle_XOR(node, weight, edge_dict)

if __name__ == "__main__":
    t = int(input())
    n_s = {}
    m_s = {}
    edge_dicts = {}
    queries = {}
    for i in range(t):
        n_m = list(map(int, input().split()))
        n, m = n_m[0], n_m[1]
        n_s[i] = n
        m_s[i] = m
        for _ in range(n-1):
            u_v_w = list(map(int, input().split()))
            u = u_v_w[0]
            v = u_v_w[1]
            w = u_v_w[2]
            edge_pair = tuple(sorted((u,v)))
            if i not in edge_dicts:
                edge_dicts[i]= {edge_pair: w}
            else:
                edge_dicts[i][edge_pair] = w
        
        for j in range(m):
            query_str = input().split()
            if query_str[0] == "^":
                query_tuple = ("^", int(query_str[1]))
            else:
                node, weight = int(query_str[1]), int(query_str[2])
                query_tuple = ("?", node, weight)

            if i not in queries:
                queries[i] = {j:query_tuple}
            else:
                queries[i][j]= query_tuple
    
    for i in range(t):
        n, m, edge_dict, query_set = n_s[i], m_s[i], edge_dicts[i], queries[i]
        process_case(n, m, edge_dict, query_set)