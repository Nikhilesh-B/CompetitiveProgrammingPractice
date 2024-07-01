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

int process_case(int n, int k)
{
    int full_periods = n - 1;
    return full_periods * k + 1;
}

int main()
{
    int t{}, n{}, k{};
    cin >> t;

    vector<int> answers{};

    while (t--)
    {
        cin >> n >> k;
        answers.push_back(process_case(n, k));
    }

    for (auto a : answers)
    {
        cout << a << endl;
    }
}