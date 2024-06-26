#include <iostream>
using namespace std;

void process_case(long long x, long long y, long long z, long long k)
{
    vector<long long> box_sides = {x, y, z};
    sort(box_sides.begin(), box_sides.end());
    x = box_sides[2];
    y = box_sides[1];
    z = box_sides[0];
    // cout << "x is" << x << endl;
    // cout << "y is" << y << endl;
    // cout << "z is" << z << endl;
    long long max_pos = 0;
    for (long long s1 = 1; s1 <= x; s1++)
    {
        for (long long s2 = 1; s2 <= y; s2++)
        {
            if (k % (s1 * s2) == 0)
            {
                long long s3 = k / (s1 * s2);
                // cout << "s1 is " << s1 << " s2 is " << s2 << " s3 is " << s3 << endl;
                if (s3 <= z)
                {
                    max_pos = max((x - s1 + 1) * (y - s2 + 1) * (z - s3 + 1), max_pos);
                }
            }
        }
    }
    cout << max_pos << endl;
}

int main()
{
    int t{};
    cin >> t;
    long long cases[t][4];
    int count{0};

    while (count < t)
    {
        for (int j = 0; j < 4; j++)
        {
            cin >> cases[count][j];
        }
        count++;
    }

    int x{}, y{}, z{}, k{};
    for (int i = 0; i < t; i++)
    {
        x = cases[i][0];
        y = cases[i][1];
        z = cases[i][2];
        k = cases[i][3];
        process_case(x, y, z, k);
    }
}