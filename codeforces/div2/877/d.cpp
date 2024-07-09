#include <iostream>
#include <vector>
#include <iomanip>
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

template <typename T>
void printVectorNL(const std::vector<T> &vec)
{
    for (const auto &elem : vec)
    {
        std::cout << elem << std::endl;
    }
}

string solve(string str, int n)
{
    // right pass
    int last_double_close = -1;
    int last_open_imbalance = -1;
    int right_imbalance_value = 0;

    for (int i = 0; i < n; i++)
    {
        str[i] == '(' ? right_imbalance_value += 1 : right_imbalance_value -= 1;
        if (i < n - 1 && str[i] == ')' && str[i + 1] == ')')
            last_double_close = i + 1;
        if (right_imbalance_value > 0)
            last_open_imbalance = i;
    }

    // left pass
    int first_double_open = -1;
    bool first_double_open_flag = false;
    int first_closed_imbalance = -1;
    bool first_closed_imbalance_flag = false;

    int left_imbalance_value = 0;

    for (int i = 0; i < n; i++)
    {
        str[i] == ')' ? left_imbalance_value += 1 : left_imbalance_value -= 1;
        if (i < n - 1 && str[i] == '(' && str[i + 1] == '(' && !first_double_open_flag)
        {
            first_double_open_flag = i + 1;
            first_double_open_flag = true;
        }
        if (!first_closed_imbalance_flag && left_imbalance_value > 0)
        {
            first_closed_imbalance = i;
            first_double_open_flag = i + 1;
            first_closed_imbalance_flag = true;
        }
    }

    // we have enough and it's not odd
    bool cond1 = (!(right_imbalance_value) || last_double_close != -1) && (!(left_imbalance_value) || first_double_open != -1);

    bool cond2 = (!(right_imbalance_value % 2) && !(left_imbalance_value % 2));

    bool cond3 =  (!(right_imbalance_value) || (last_double_close<first_closed_imbalance)) && (!(left_imbalance_value) || (first_double_open));
}

int main()
{
    int n, q, qidx;
    cin >> n;
    string str;
    cin >> str;

    vector<string> answers(q, "");

    for (int i = 0; i < q; ++i)
    {
        cin >> qidx;
        str[qidx] == '(' ? str[qidx] = ')' : str[qidx] = '(';
        answers[i] = solve(str, n);
    }

    printVectorNL(answers);
}