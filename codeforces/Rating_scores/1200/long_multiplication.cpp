#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <unordered_map>
#include <climits>

using namespace std;

void print_num(vector<char> &a)
{
    for (auto ai : a)
    {
        cout << ai;
    }
    cout << endl;
}

int main()
{
    int t{};
    cin >> t;
    cin.ignore(); // To ignore the newline after reading t

    while (t--)
    {
        unordered_map<int, int> xdigits = {};
        unordered_map<int, int> ydigits = {};

        int i = 0;
        char ch;

        // Reading the first number
        while (cin.get(ch))
        {
            if (ch != '\n')
            {
                int val = ch - '0';
                xdigits[i] = val;
                ++i;
            }
            else
            {
                break;
            }
        }

        int j = 0;
        // Reading the second number
        while (cin.get(ch))
        {
            if (ch != '\n')
            {
                int val = ch - '0';
                ydigits[j] = val;
                ++j;
            }
            else
            {
                break;
            }
        }

        vector<char> fnum{};
        vector<char> snum{};

        bool switchrules = false;
        for (int k = 0; k < i; ++k)
        {
            if (!switchrules)
            {
                if (xdigits[k] > ydigits[k])
                {
                    fnum.push_back(xdigits[k] + '0');
                    snum.push_back(ydigits[k] + '0');
                    switchrules = true;
                }
                else if (xdigits[k] < ydigits[k])
                {
                    fnum.push_back(ydigits[k] + '0');
                    snum.push_back(xdigits[k] + '0');
                    switchrules = true;
                }
                else
                {
                    fnum.push_back(ydigits[k] + '0');
                    snum.push_back(xdigits[k] + '0');
                }
            }
            else
            {
                if (xdigits[k] < ydigits[k])
                {
                    fnum.push_back(xdigits[k] + '0');
                    snum.push_back(ydigits[k] + '0');
                }
                else
                {
                    fnum.push_back(ydigits[k] + '0');
                    snum.push_back(xdigits[k] + '0');
                }
            }
        }

        print_num(fnum);
        print_num(snum);
    }

    return 0;
}