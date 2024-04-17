#include<iostream>
#include<algorithm>
#include<vector>
using namespace std; 

bool by_first_asc(const pair<int,int>& a, const pair<int,int>& b) {
	return a.first > b.first;
}

int main() {
	int n, k;
	cin >> n >> k; 

	vector<pair<int,int>> seq(n); 
	for (int i = 0; i < n; ++i) {
		cin >> seq[i].first;
		seq[i].second = i; 
	}

	sort(seq.begin(), seq.end(), by_first_asc);

	int sum = 0;
	cout << "Elements: "; 
	for (int i = 0; i < k; ++i) {
		sum += seq[i].first;
		cout << seq[i].first << " ";
	}

	cout << endl << "Result: " << sum << endl; 
	cout << "Index: ";
	for (int i = 0; i < k; ++i) {
		cout << seq[i].second << " ";
	}
	cout << endl; 

	return 0; 
}
