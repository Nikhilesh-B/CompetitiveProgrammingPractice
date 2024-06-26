#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <unordered_map>
#include <climits>

using namespace std;

int process_case(int l, int r, int a)
{
    int left_divide = l / a;
    int right_divide = r / a;
    if (left_divide == right_divide)
    {
        return right_divide + r % a;
    }
    else
    {
        if (r % a != a - 1)
        {
            return (right_divide - 1) + (a - 1);
        }
        else
        {
            return (right_divide) + (a - 1);
        }
    }
}

int main()
{
    int t{};
    cin >> t;

    vector<int> answers{};
    while (t--)
    {
        int l{}, r{}, a{};
        cin >> l >> r >> a;
        answers.push_back(process_case(l, r, a));
    }
    for (int a : answers)
    {
        cout << a << endl;
    }
}