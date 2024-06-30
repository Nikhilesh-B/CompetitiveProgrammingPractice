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

vector<ipair> get_neighbors(ipair node, vector<cpair> &a, int n)
{
    int position = node.first;
    int idx = node.second;
    int distance = a[idx].first;
    char direction = a[idx].second;

    vector<ipair> neighbors = {};

    int new_idx = idx + 1;
    if (direction == '0')
    {
        neighbors.push_back(make_pair((position + distance) % n, new_idx));
    }
    else if (direction == '1')
    {
        neighbors.push_back(make_pair((position - distance + n) % n, new_idx));
    }
    else
    {
        neighbors.push_back(make_pair((position - distance + n) % n, new_idx));
        neighbors.push_back(make_pair((position + distance) % n, new_idx));
    }

    return neighbors;
}

void process_case(int n, int m, int x, vector<cpair> &a)
{
    set<int> answers;
    set<ipair> explored{};

    deque<ipair> lifo_stack = {{x, 0}};

    while (!lifo_stack.empty())
    {
        ipair node = lifo_stack.back();
        lifo_stack.pop_back();
        if (node.second == m)
        {
            answers.insert(node.first);
            continue;
        }
        vector<ipair> neighbors = get_neighbors(node, a, n);
        explored.insert(node);
        for (auto &n : neighbors)
        {
            if (explored.find(n) == explored.end())
                lifo_stack.push_back(n);
        }
    }

    if (answers.find(0) != answers.end())
    {
        answers.erase(0);
        answers.insert(n);
    }

    cout << answers.size() << endl;
    for (int ai : answers)
        cout << ai << " ";
    cout << endl;
}

int main()
{
    int t{};
    cin >> t;
    while (t--)
    {
        int n{}, m{}, x{};
        cin >> n >> m >> x;
        vector<cpair> a(m);
        for (int i = 0; i < m; ++i)
        {
            cin >> a[i].first >> a[i].second;
        }
        process_case(n, m, x, a);
    }
    return 0;
}