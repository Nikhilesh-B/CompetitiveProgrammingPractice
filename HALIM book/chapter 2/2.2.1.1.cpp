#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<int> vec = {23,4,5,100,2,1};
    sort(vec.begin(), vec.end());   

    for(int i: vec){
        cout << i << " ";
    }

    cout << endl;

    return 0;
}