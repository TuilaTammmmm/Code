#include <bits/stdc++.h>
using namespace std;
int main(){
	int t; cin >> t;
	string s1="ABBADCCABDCCABD";
	string s2="ACCABCDDBBCDDBB";
	while(t--){
		int n, cnt=0; cin >> n;
		char a[15];
		for(int i=0;i<15;i++){
			cin >> a[i];
		}  
		if(n==101){
			for(int i=0;i<15;i++){
				if(a[i]==s1[i]){
					++cnt;
				}
			}
		}
		if(n==102){
			for(int i=0;i<15;i++){
				if(a[i]==s2[i]){
					++cnt;
				}
			}
		}
		float diem=1.0*cnt/15*10;
		cout << fixed << setprecision(2) << diem << endl;
	}
}