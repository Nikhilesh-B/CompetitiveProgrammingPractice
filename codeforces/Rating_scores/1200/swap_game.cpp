#include <iostream>
#include <string>
#include <vector>

using namespace std;

string process_case(vector<int> &a)
{
    int sum = 0;
    for (int x : a)
    {
        sum += x;
    }
    sum -= 1;

    if (sum % 2 == 1)
    {
        return "BOB";
    }

    else
    {
        return "ALICE";
    }
}

int main()
{
    int t{}, n{}, x{};
    vector<string> answers;

    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        vector<int> numbers{};
        cin >> n;

        for (int j = 0; j < n; j++)
        {
            cin >> x;
            numbers.push_back(x);
        }
        answers.push_back(process_case(numbers));
    }

    for (int i = 0; i < t; ++i)
    {
        cout << answers[i] << endl;
    }
}
