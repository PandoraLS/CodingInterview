//参考链接：https://www.geeksforgeeks.org/sum-of-the-first-n-prime-numbers/
// C++ implementation of above solution
#include <bits/stdc++.h>
using namespace std;
#define MAX 10000

// Create a boolean array "prime[0..n]" and initialize
// all entries it as true. A value in prime[i] will
// finally be false if i is Not a prime, else true.
bool prime[MAX + 1];
void SieveOfEratosthenes() {
    //对前sqrt(MAX)个数进行判断
    memset(prime, true, sizeof(prime));  //memset 函数是内存赋值函数，用来给某一块内存空间进行赋值的；
    prime[0] = false, prime[1] = false;
    for (int p = 2; p * p <= MAX; p++) {
        // If prime[p] is not changed, then it is a prime
        if (prime[p] == true) {
            // Set all multiples of p to non-prime
            for (int i = p * 2; i <= MAX; i += p) {
                prime[i] = false;
            }
        }
    }
}

// find the sum of 1st N prime numbers
void solve(int n) {
    // count of prime numbers
    int count = 0, num = 1;
    while (count < n) {
        // if the nuber is prime, cout it
        if (prime[num]) {
            cout << num << " ";
            // increase the count
            count++;
        }
        // get to next number
        num++;
    }
}

// Driver code
int main(void) {
    // create the sieve
    SieveOfEratosthenes();
    int n = 0;
    cout << "求前n个质数：（请输入n）:\n";
    while (cin >> n) {
        solve(n);
        cout << endl;
    }
    return 0;
}
