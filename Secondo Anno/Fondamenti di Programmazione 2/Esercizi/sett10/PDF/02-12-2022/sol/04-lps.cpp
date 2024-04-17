#include<iostream>
#include<vector>
#include<string>
#include<cassert>
#include<algorithm>
using namespace std; 

int compute_lps(const string& s, vector<vector<int>>& S, int i, int j) {
	assert( i >= 0 and j >= 0 and i < s.size() and j < s.size() );

	if (S[i][j] != -1) return S[i][j];

	if (s[i] == s[j]) {
		S[i][j] = 2 + compute_lps(s, S, i+1, j-1); 
	} else {
		S[i][j] = max(compute_lps(s, S, i+1, j), compute_lps(s, S, i, j-1));
	}
	return S[i][j];
}



int main() {
	string s;
	cin >> s;

	int n = s.size();
	vector<vector<int>> S(n, vector<int>(n, -1));

	for (int i = 0; i < n; ++i) {
		S[i][i] = 1;

		for (int j = 0; j < i; ++j) {
			S[i][j] = 0;
		}
	}

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			cout << S[i][j] << " ";
		}
		cout << endl; 
	}

	int solution_length = compute_lps(s, S, 0, s.size()-1);

	cout << "Done" << endl; 
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			cout << S[i][j] << " ";
		}
		cout << endl; 
	}

	cout << solution_length << endl;

	string left = "", right = ""; 
	int i = 0;
	int j = s.size()-1;

	string solution = ""; 

	while (i < j) {
		if ( s[i] == s[j] ) {
			left = left + s[i];
			right = s[j] + right;
			++i;
			--j;
		} else if (S[i+1][j] > S[i][j-1]) {
			++i;
		} else {
			--j;
		}
	}

	if (i == j) {
		left = left + s[i];
		solution = left + right;
	} else {
		solution = left + right; 
	}

	cout << solution << endl; 

	return 0; 
}


