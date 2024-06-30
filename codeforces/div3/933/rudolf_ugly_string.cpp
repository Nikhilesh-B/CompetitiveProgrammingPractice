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

typedef pair<int, char> cpair;
typedef pair<int, int> ipair;

vector<ipair> get_neigbors(ipair node, vector<cpair> &a, int n)
{
    int position = node.first;
    int idx = node.second;
    int distance = a[idx].first;
    char direction = a[idx].second;

    vector<ipair> neighs = {};

    int new_idx = idx + 1;
    if (direction == '0')
    {
        neighs.push_back(make_pair((position + distance) % n, new_idx));
    }
    else if (direction == '1')
    {
        neighs.push_back(make_pair((position - distance) % n, new_idx));
    }
    else
    {
        neighs.push_back(make_pair((position - distance) % n, new_idx));
        neighs.push_back(make_pair((position + distance) % n, new_idx));
    }

    return neighs;
}

void process_case(int n, int m, int x, vector<cpair> &a)
{
    cout << n << m << x;
    vector<int> answers;
    set<ipair> explored{};

    deque<ipair> lifo_stack = {{x, 0}};

    while (!lifo_stack.empty())
    {
        ipair node = lifo_stack[lifo_stack.size() - 1];
        lifo_stack.pop_back();
        if (node.second == m)
        {
            answers.push_back(node.first);
        }
        vector<ipair> neighbors = get_neigbors(node, a, n);
        explored.insert(node);
        for (auto n : neighbors)
        {
            if (explored.find(n) == explored.end())
                lifo_stack.push_back(n);
        }
    }

    sort(answers.begin(), answers.end());

    cout << answers.size() << endl;
    for (int ai : answers)
        cout << ai << " ";
    cout << endl;
}

int main()
{
    int t{};
    cin >> t;
    vector<vector<int>> answers{};
    while (t--)
    {
        int n{}, m{}, x{};
        int r{};
        char c{}, space{};
        cin >> n >> m >> x;
        vector<cpair> a{};
        for (int i = 0; i < m; ++i)
        {
            cin >> r;
            cin >> space;
            cin >> c;
            a.push_back(make_pair(r, c));
        }
        process_case(n, m, x, a);
    }
}
