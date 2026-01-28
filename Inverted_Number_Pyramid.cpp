/*
Input: 5
1        1
12      21
123    321
1234  4321
1234554321
*/
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Input: " << endl;
    cin >> n;
    for(int i=1; i<=n; i++){
        for(int j=1; j<=2*n; j++){
            if(j<=i){cout << j;}
            else if(j<=((2*n)-i)){cout << " ";}
            else cout << ((2*n)+1-j);
        }
        cout << "\n";
    }
    return 0;
}
