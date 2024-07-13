#include <iostream>
#include <vector>
#include <queue>
#include <set>

using namespace std;

string solve(int n, int m, int k, string &a) {
    int goal = n;
    queue<pair<int, int>> q;
    set<pair<int, int>> explored;

    q.push({-1, 0});

    while (!q.empty()) {
        pair<int, int> current = q.front();
        q.pop();
        int c_pos = current.first;
        int c_swim = current.second;

        if (c_pos == goal) {
            return "YES";
        }

        if (explored.count(current) == 0) {
            explored.insert(current);

            if (c_pos == -1 || a[c_pos] == 'L') {
                for (int j = 1; j <= m; ++j) {
                    if (c_pos + j == n && explored.count({c_pos + j, c_swim}) == 0) {
                        q.push({c_pos + j, c_swim});
                        break;
                    } else if (a[c_pos + j] != 'C' && explored.count({c_pos + j, c_swim}) == 0) {
                        q.push({c_pos + j, c_swim});
                    }
                }
            }

            if (c_swim < k) {
                if (c_pos + 1 == n && explored.count({c_pos + 1, c_swim + 1}) == 0) {
                    q.push({c_pos + 1, c_swim + 1});
                } else if (a[c_pos + 1] != 'C' && explored.count({c_pos + 1, c_swim + 1}) == 0) {
                    q.push({c_pos + 1, c_swim + 1});
                }
            }
        }
    }

    return "NO";
}

int main() {
    int t;
    cin >> t;
    vector<string> answers;

    for (int i = 0; i < t; ++i) {
        int n, m, k;
        cin >> n >> m >> k;

        string a;
        cin >> a;

        answers.push_back(solve(n, m, k, a));
    }

    for (const string &answer : answers) {
        cout << answer << endl;
    }

    return 0;
}