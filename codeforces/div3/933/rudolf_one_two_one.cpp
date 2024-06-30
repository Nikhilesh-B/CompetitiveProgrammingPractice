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

string process_case(int n, vector<int> &a)
{
    int count = 0;
    int i = 0;
    int j = a.size() - 1;
    while (i < j)
    {
        if (count % 2 == 0)
        {
            int increment = a[i];
            a[i] -= increment;
            a[i + 1] -= 2 * increment;
            a[i + 2] -= increment;
            if (a[i] < 0 || a[i + 1] < 0 || a[i + 2] < 0)
                return "NO";
            i++;
        }
        else
        {
            int increment = a[j];
            a[j] -= increment;
            a[j - 1] -= 2 * increment;
            a[j - 2] -= increment;
            if (a[j] < 0 || a[j - 1] < 0 || a[j - 2] < 0)
                return "NO";
            j--;
        }
        count += 1;
    }
    for (int ai : a)
    {
        if (ai != 0)
            return "NO";
    }
    return "YES";
}

int main()
{
    int t{};
    cin >> t;
    vector<string> answers{};
    while (t--)
    {
        int n{}, x{};
        cin >> n;
        vector<int> a{};
        for (int i = 0; i < n; ++i)
        {
            cin >> x;
            a.push_back(x);
        }

        answers.push_back(process_case(n, a));
    }

    for (auto a_i : answers)
    {
        cout << a_i << endl;
    }
}
