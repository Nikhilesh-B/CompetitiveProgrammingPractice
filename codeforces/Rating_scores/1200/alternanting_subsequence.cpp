#include <iostream>
#include <vector>
#include <algorithm>
#include <string>


using namespace std;

vector<int> getleftcosts(vector<int> &c)
{
    vector<int> leftcosts{};
    int leftsum = 0;
    for (int j : c)
    {
        leftsum += j;
        leftcosts.push_back(leftsum);
    }
    return leftcosts;
}

vector<int> getrightcosts(vector<int> &c)
{
    vector<int> rightcosts{};
    int rightsum = 0;
    for (int j = c.size() - 1; j >= 0; --j)
    {
        rightsum += c[j];
        rightcosts.push_back(rightsum);
    }
    reverse(rightcosts.begin(), rightcosts.end());
    return rightcosts;
}



int process_case(vector<int> &a, int n){
    int total = 0;
    for (int a_i: a){
        total += a_i;
    }

    vector<int> leftsums = getleftcosts(a);
    vector<int> rightsums = getrightcosts(a);

    //we need to find the longest alternating segments first







}


int main(){
    int t{};
    vector<int> answers{};
    while(t--){
        int n {};
        vector<int> nums{};
        cin >> n;
        while(n--){
            int x{};
            cin >> x;
            nums.push_back(x);
        }
        int ans = process_case(nums, n);
        answers.push_back(ans);
    }
    for (int ans: answers){
        cout << ans << endl;
    }
}