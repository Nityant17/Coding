/*
Enter n:4
4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 
*/
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Input: " << endl;
    cin >> n;
    int a[(2*n)-1][(2*n)-1];
    int center = n-1;
    for (int i=0; i<((2*n)-1); i++) {
        for (int j=0; j<((2*n)-1); j++) {
            a[i][j]=max(abs(i-center),abs(j-center))+1;
            cout << a[i][j];
        }
        cout << "\n";
    }
    return 0;
}
