// prim's algorithm is really simple
// 2 sets, unexplored and explored;
// at each step in the exploration of the graph find a cut, pick the minimum edge value and then add it
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <unordered_map>
#include <unordered_set>
#include <list>
#include <map>
#include <set>
#include <climits>
#include <queue>

using namespace std;

typedef pair<int, int> ipair;
typedef tuple<int, int, int> itriple;

vector<itriple> return_outboud_edges(vector<vector<int>> &adj_matrix, int u)
{
    vector<itriple> outbound_edges = {};
    int n = adj_matrix.size();

    for (int i = 0; i < n; ++i)
    {
        int v = i;
        if (adj_matrix[u][v])
        {
            itriple edge_weight = tuple(u, v, adj_matrix[u][v]);
            outbound_edges.push_back(edge_weight);
        }
    }
    return outbound_edges;
}

vector<vector<int>> prims_algorithm(vector<vector<int>> &adj_matrix)
{
    int n = adj_matrix.size();
    vector<vector<int>> MST(n, vector<int>(n, 0));
    int counter = 0;
    vector<bool> included(n, false);

    auto compareTriple = [](itriple t1, itriple t2)
    {
        return get<2>(t1) > get<2>(t2); // for minimum order
    };

    priority_queue<itriple, vector<itriple>, decltype(compareTriple)> pq;
    for (itriple triple : return_outboud_edges(adj_matrix, 0))
    {
        pq.push(triple);
    }
    included[0] = true;
    counter += 1;

    while (counter < n && !pq.empty())
    {
        while (included[get<1>(pq.top())] && !pq.empty())
        {
            pq.pop();
        }
        itriple new_triple = pq.top();
        pq.pop();
        int u{get<0>(new_triple)}, v{get<1>(new_triple)}, weight{get<2>(new_triple)};
        MST[u][v] = weight;
        MST[v][u] = weight;
        included[v] = true;
        counter += 1;
        for (auto triple : return_outboud_edges(adj_matrix, v))
        {
            pq.push(triple);
        }
    }
    return MST;
}

void print_matrix(vector<vector<int>> &adj_matrix)
{
    int n = adj_matrix.size();
    for (int i = 0; i < n; ++i)
    {
        cout << "[ ";
        for (int j = 0; j < n; ++j)
        {
            cout << adj_matrix[i][j] << " ";
        }
        cout << "]" << endl;
    }
}

int main()
{
    vector<vector<int>> adj_matrix = {{0, 2, 1, 2, 1},
                                      {2, 0, 1, 1, 13},
                                      {1, 1, 0, 2, 12},
                                      {2, 1, 2, 0, 5},
                                      {1, 13, 12, 5, 0}};

    vector<vector<int>> MST = prims_algorithm(adj_matrix);
    print_matrix(MST);
}
