#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <unordered_map>
#include <climits>

using namespace std;
int process_case(int n, int l, int r, vector<int> &cards)
{
    int i = 0;
    int j = 0;
    int ans = 0;
    int incremental_sum = 0;
    while (i < n)
    {
        while (incremental_sum < l && j < n)
        {
            incremental_sum += cards[j];
            ++j;
        }
        if (incremental_sum >= l && incremental_sum <= r)
        {
            ans += 1;
            incremental_sum = 0;
            i = j;
        }
        else
        {
            incremental_sum -= cards[i];
            ++i;
        }
    }
    return ans;
}
int main()
{
    int t;
    cin >> t;
    vector<int> answers;
    while (t--)
    {
        int n{}, l{}, r{}, x{};
        vector<int> cards{};
        cin >> n >> l >> r;
        for (int i = 0; i < n; ++i)
        {
            cin >> x;
            cards.push_back(x);
        }
        answers.push_back(process_case(n, l, r, cards));
    }

    for (int ans : answers)
    {
        cout << ans << endl;
    }
}
