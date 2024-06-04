#include <iostream>
#include <vector>

using namespace std;



struct fraction {
    int num {};
    int den {}; 
};

bool compare_fractions(fraction& a, fraction& b){
    return a.num * b.den < b.num * a.den;
}


void sort_fractions(){
    vector<fraction> vec = {{1,2}, {3,4}, {1,3}, {2,3}, {1,4}};
    sort(vec.begin(), vec.end(), compare_fractions);
    for(fraction i: vec){
        cout << i.num << "/" << i.den << " ";
    }
    cout << endl;
}


void sort_integers(){
    vector<int> vec = {23,4,5,100,2,1};
    sort(vec.begin(), vec.end());
    for(int i: vec){
        cout << i << " ";
    }
    cout << endl;
}

void sort_last_names(){
    vector<string> vec = {"Ali", "Nikhilesh", "Sai", "rohan", "rahul", "Glenn", "Brett"};
    sort(vec.begin(), vec.end());
    for(string i: vec){
        cout << i << " ";
    }
    cout << endl;
}


void sort_first_names(){
    vector<string> vec = {"Ali", "Nikhilesh", "Sai", "rohan", "rahul", "Glenn", "Brett"};
    sort(vec.begin(), vec.end(), greater<string>());
    for(string i: vec){
        cout << i << " ";
    }
    cout << endl;
}

int main(){
    sort_integers();
    sort_last_names();
    sort_first_names();
    sort_fractions();
    return 0;
}