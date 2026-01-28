/*
Input: 7
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
0 1 0 1 0 1 
1 0 1 0 1 0 1
*/
#include <iostream>
using namespace std;

int main() {
    int n, start=1;
    cout << "Input: " << endl;
    cin >> n;
    for(int i=1; i<=n; i++){
        int term = start;
        for(int j=1; j<=i; j++){
            if(term==1){
                cout << term << " ";
                term=0;
            }
            else{
                cout << term << " ";
                term=1;
            }
        }
        cout << "\n";
        if(start==1){start=0;}
        else{start=1;}
    }
    return 0;
}
