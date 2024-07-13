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
void printVectorNL(const std::vector<T> &set)
{
    for (const auto &elem : set)
    {
        std::cout << elem << std::endl;
    }
}

int solve()
{
    int a, b, c;
    cin >> a >> b >> c;
    int a_copy = a;
    int b_copy = b;
    int c_copy = c;

    int mx = a * b * c;
    for (int i = 0; i < 3; i++)
    {
        if (i == 0)
            a++;
        else if (i == 1)
            b++;
        else
            c++;

        for (int j = 0; j < 3; j++)
        {
            if (j == 0)
                a++;
            else if (j == 1)
                b++;
            else
                c++;

            for (int k = 0; k < 3; k++)
            {
                if (k == 0)
                    a++;
                else if (k == 1)
                    b++;
                else
                    c++;
                for (int l = 0; l < 3; l++)
                {
                    if (l == 0)
                        a++;
                    else if (l == 1)
                        b++;
                    else
                        c++;
                    for (int m = 0; m < 3; m++)
                    {
                        if (m == 0)
                            a++;
                        else if (m == 1)
                            b++;
                        else
                            c++;

                        mx = max(mx, a * b * c);

                        a = a_copy;
                        b = b_copy;
                        c = c_copy;
                    }
                }
            }
        }
    }
    return mx;
}

int main()
{
    int t;
    cin >> t;
    vector<int> answers(t, 0);

    for (int i = 0; i < t; i++)
        answers[i] = solve();

    printVectorNL(answers);
}
