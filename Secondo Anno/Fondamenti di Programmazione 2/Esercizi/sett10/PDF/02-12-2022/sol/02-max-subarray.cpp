#include<iostream>
#include<vector>
#include<algorithm>
using namespace std; 

int main() {
	int n; 
	cin >> n; 

	vector<int> seq(n);
	for (int i = 0; i < n; ++i) {
		cin >> seq[i];
	}

	vector<int> S(n);
	S[0] = seq[0];

	int best_sum = 0;
	int best_i = 0;
	int best_j = 0; 

	int curr_i = 0;
	int curr_j = 0; 

	for (int i = 1; i < n; ++i) {
		if (S[i-1]+seq[i] > seq[i]) {
			++curr_j;
		} else {
			curr_i = curr_j = i;
		}

		S[i] = max(S[i-1]+seq[i],seq[i]);
		if (S[i] > best_sum) {
			best_i = curr_i;
			best_j = curr_j;
			best_sum = S[i]; 
		}
	}

	cout << best_sum << ", " << best_i << ", " << best_j << endl; 
	return 0; 
}
