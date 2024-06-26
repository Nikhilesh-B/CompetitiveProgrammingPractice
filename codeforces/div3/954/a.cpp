#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <unordered_map>
#include <climits>

using namespace std;

int process_case(int a1, int a2, int a3)
{
    int min_sum = INT_MAX;
    int new_sum{};
    for (int a = 1; a <= 10; ++a)
    {
        new_sum = abs(a - a1) + abs(a - a2) + abs(a - a3);
        min_sum = min(min_sum, new_sum);
    }
    return min_sum;
}

int main()
{
    int t{};
    cin >> t;

    vector<int> answers{};

    int a1{}, a2{}, a3{};
    for (int i = 0; i < t; ++i)
    {
        cin >> a1 >> a2 >> a3;
        answers.push_back(process_case(a1, a2, a3));
    }

    for (int i = 0; i < t; ++i)
    {
        cout << answers[i] << endl;
    }
}