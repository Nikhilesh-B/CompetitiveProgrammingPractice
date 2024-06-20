#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <string>

using namespace std;

string get_num_str(int n, int k, int t)
{
    string rstr = "";
    if (t == 0)
    {   
        if(n%k==0){
            for (int i=0;i<n/k;++i){
                rstr += 
            }
        }
    }
    else if (t == 1)
    {
    }
    else
    {
    }
}

string process_case(int n, int k)
{
    if (k > n)
    {
        return "NO";
    }
    bool n_even = (n % 2 == 0);
    bool k_even = (k % 2 == 0);

    if (!n_even && k_even)
    {
        return "NO";
    }

    else if (!n_even && !k_even)
    {
        string ans = get_num_str(n, k, 0);
        return "YES";
    }

    else if (n_even && !k_even)
    {
        if (n / 2 >= k)
        {
            string ans = get_num_str(n, k, 1);
            return "YES";
        }
        else
        {
            return "NO";
        }
    }
    else
    {
        string ans = get_num_str(n, k, 2);
        return "YES";
    }
}

int main()
{
    int t{};

    cin >> t;
    vector<string> answers{};

    while (t--)
    {
        int n{}, k{};
        cin >> n >> k;
        answers.push_back(process_case(n, k));
    }

    for (string s : answers)
    {
        cout << s << endl;
    }
}