#include <bits/stdc++.h>
using namespace std;

vector<string> vc;
string s;

int main(){
	while (getline(cin,s)) 
		if (s.length() != 0)
			vc.push_back(s);
			
	system("cls");
	for (int i=0;i<vc.size();i++){
		cout<<(i+1)*10<<' '<<vc[i]<<endl;
	}
	
	return 0;
} 
