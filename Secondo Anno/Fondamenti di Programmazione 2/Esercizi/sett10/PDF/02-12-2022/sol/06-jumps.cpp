#include<iostream>
#include<vector>
#include<algorithm>
using namespace std; 



int main() {
	int n; 
	cin >> n; 

	vector<int> cells(n);
	for (int i = 0; i < n; ++i) cin >> cells[i]; 

	vector<int> S(n);
	S[n-1] = 0;

	for (int i = n-2; i >= 0; --i) {
		int max_reachable_cell = min(i + cells[i], n-1);
		cout << "Dalla posizione " << i << " posso raggiungere fino alla posizione " << max_reachable_cell << endl; 

		int min_jumps_in_range = n;

		for (int k = i+1; k <= max_reachable_cell; ++k) {
			min_jumps_in_range = min(min_jumps_in_range, S[k]);
		}

		S[i] = 1 + min_jumps_in_range;
		cout << "Dalla posizione " << i << " ci vogliono " << S[i] << " salti!" << endl; 
	}

	cout << S[0] << endl; 

	return 0; 
}
