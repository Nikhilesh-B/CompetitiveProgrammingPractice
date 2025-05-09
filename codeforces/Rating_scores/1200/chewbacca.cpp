#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <string>

using namespace std;
typedef long long ll;

void process_case(long long x)
{
    
    string numstr = to_string(x);
    string new_str = "";
    int idx = 0;
    for (char c : numstr)
    {
        int char_val = c - '0';
        if (char_val >= 5 && !(idx == 0 && char_val==9))
        {
            char new_char = (9 - char_val) + '0';
            new_str.push_back(new_char);
        }
        else
        {
            new_str.push_back(c);
        }
        idx += 1;
    }
    long long new_num = stoll(new_str);
    if (new_num == 0)
    {
        cout << x;
    }
    else
    {
        cout << new_num;
    }
}

int main()
{
    long long x;
    cin >> x;
    process_case(x);
}