#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <vector>
#include <unordered_map>
#include <climits>

using namespace std;

void process_case(int n, vector<int> &a)
{
    int odd_count = {0};
    int even_count = {0};

    for (int idx = 0; idx < n; ++idx)
    {
        if (a[idx] % 2 == 0)
        {
            odd_count += 1;
        }
        else
        {
            even_count += 1;
        }

        if (odd_count >= 1 && even_count >= 1)
        {
            break;
        }
    }

    if (odd_count >= 1 && even_count >= 1)
    {
        sort(a.begin(), a.end());
    }

    for (int ai : a)
    {
        cout << ai << " ";
    }
}

int main()
{
    int n{};
    vector<int> a{};
    cin >> n;
    int ai{};
    for (int i = 0; i < n; ++i)
    {
        cin >> ai;
        a.push_back(ai);
    }

    process_case(n, a);
}
