#include <bits/stdc++.h>
using namespace std;
int ss(int n){
	int chan=0, le=0;
	while(n!=0){
		if((n%10)%2==0) ++chan;
		else ++le;
		n/=10;
	}
	if(chan==le) return 1;
	else return 0;
}
int main(){
	int n, cnt=0; cin >> n;
	for(int i=pow(10,n-1);i<pow(10,n);i++){
		if(ss(i)==1){
			++cnt;
			cout << i << " ";
			if(cnt%10==0){
				cout << endl;
			}
		}
	}
}