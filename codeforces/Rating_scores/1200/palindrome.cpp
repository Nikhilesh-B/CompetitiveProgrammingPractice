#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <string>

using namespace std;

bool all_ones(string &s)
{
    for (char a : s)
    {
        if (a == '0')
        {
            return false;
        }
    }
    return true;
}

bool is_palindrome(string &s)
{
    for (int i = 0; i < s.size(); ++i)
    {
        int reverse_idx = (s.size() - 1 - i);
        if (s[i] != s[reverse_idx])
        {
            return false;
        }
    }
    return true;
}

void change_one(string &s)
{
    for (int i = 0; i < s.size(); ++i)
    {
        if (s[i] == '0')
        {
            s[i] = '1';
        }
    }
}

void make_palindrome(string &s)
{
    for (int i = 0; i < s.size(); ++i)
    {
        int reverse_idx = (s.size() - 1 - i);
        if (s[i] != s[reverse_idx])
        {
            if (s[i] == '0')
            {
                s[i] = '1';
            }
            else
            {
                s[reverse_idx] = '1';
            }
        }
        else if (i == reverse_idx && s[i] == 0)
        {
            s[i] = '1';
        }
    }
}

string process_case(int num)
{
    int alice_spend = 0;
    int bob_spend = 0;

    string numstr = to_string(num);

    int i = 0;
    bool last_play_reverse = false;
    while (!all_ones(numstr))
    {
        if (is_palindrome(numstr))
        {
            if (i % 2 == 0)
            {
                alice_spend += 1;
            }
            else
            {
                bob_spend += 1;
            }
            change_one(numstr);
            last_play_reverse = false;
        }
        else
        {
            if (!last_play_reverse)
            {
                reverse(numstr.begin(), numstr.end());
                last_play_reverse = true;
            }
            else
            {
                make_palindrome(numstr);
                if (i % 2 == 0)
                {
                    alice_spend += 1;
                }
                else
                {
                    bob_spend += 1;
                }

                last_play_reverse = false;
            }
        }
        i++;
    }

    if (alice_spend == bob_spend)
    {
        return "DRAW";
    }

    else if (alice_spend < bob_spend)
    {
        return "ALICE";
    }

    else
    {
        return "BOB";
    }
}

int main()
{
    int t{};
    vector<string> answers;

    cin >> t;

    while (t--)
    {
        int n{};
        cin >> n;
        int num{};
        cin >> num;
        answers.push_back(process_case(num));
    }

    for (string s : answers)
    {
        cout << s << endl;
    }
}