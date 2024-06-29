#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <unordered_map>
#include <set>
#include <climits>

using namespace std;

int find_zeros(string snum)
{
    int count = 0;
    for (char s : snum)
    {
        if (s == '0')
            count += 1;
    }
    return count;
}

vector<int> process_operations(vector<char> number_lst, vector<int> &operations, int n)
{
    // 0 is conjoin, 1 is add, 2 is multiply
    int multiply_count = 0;

    for (int i = 0; i < n; ++i)
    {
        if (number_lst[i] == '1')
            if (i == 0)
                operations[i] = 2;
            else if (i == n - 1)
                operations[i - 1] = 2;
            else if (number_lst[i + 1] - '0' > operations[i - 1] - '0')
                operations[i] = 2;
            else
                operations[i - 1] = 2;
    }

    int merge_idx = -1;
    int min = INT_MAX;

    for (int i = 0; i < n - 1; ++i)
    {
        if (operations[i] == 1 && operations[i + 1] == 1)
            continue;
        if (stoi(number_lst[i] + number_lst[i + 1]) < min)
        {
            min = (number_lst[i] + number_lst[i + 1]).stoi();
            merge_idx = i;
        }
    }
}

int process_case(int n, int x)
{
    string snum = to_string(x);
    vector<char> number_lst = {};

    for (char a : snum)
        number_lst.push_back(a);

    int zero_count = find_zeros(snum);

    if (zero_count > 0 && snum.length() > 3)
    {
        return 0;
    }
    else if (zero_count > 0 && snum.length() == 3)
    {
        if (zero_count > 1)
            return 0;
        // do more case work here
    }
    else
    {
        vector<int> operations(snum.length() - 1, -1);
        vector<int> new_operations = process_operations(number_lst, operations, n);
        // you need to do the following and look through all the ones in the list
    }

    return 0;
}

int main()
{
    int t{}, n{}, x{};
    cin >> t;
    vector<int> answers{};
    while (t--)
    {
        cin >> n;
        cin >> x;
        answers.push_back(process_case(n, x));
    }
    for (int ans : answers)
    {
        cout << ans << endl;
    }
}