#include <iostream>
#include <vector>

using namespace std;

int process_case(int n, int k)
{
    int m = n - 1;
    int groups = k / m;
    int leftover = k % m;
    int result{};
    if (leftover == 0)
    {
        result = groups * n - 1;
    }
    else
    {
        result = groups * n + leftover;
    }
    return result;
}

int main()
{
    int t{}, k{}, n{};
    cin >> t;
    vector<int> answers{};
    for (int i = 0; i < t; ++i)
    {
        cin >> n >> k;
        answers.push_back(process_case(n, k));
    }
    for (int i = 0; i < t; ++i)
    {
        cout << answers[i] << endl;
    }
    return 0;
}

// 1 2 3 5 6 7 9 10 11 13 14 15
// 1 2 3 4 5 6 7 8  9  10 11 12