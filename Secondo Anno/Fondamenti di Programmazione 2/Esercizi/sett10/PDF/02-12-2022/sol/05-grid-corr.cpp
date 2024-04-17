#include<iostream>
#include<vector>
using namespace std; 


int main() {
	int n, m; 
	cin >> n >> m; 

	vector<vector<int>> M(n, vector<int>(m, 0));
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cin >> M[i][j];
		}
	}

	vector<vector<int>> S(n, vector<int>(m, 0));
	S[0][0] = M[0][0];
	for (int k = 1; k < n; ++k) {
		S[k][0] = S[k-1][0] + M[k][0];
	}
	for (int k = 1; k < m; ++k) {
		S[0][k] = S[0][k-1] + M[0][k];
	}
	cout << "Matrice inserita: " << endl;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cout << M[i][j] << " ";
		}
		cout << endl; 
	}

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cout << S[i][j] << " ";
		}
		cout << endl; 
	}
	cout << "DP" << endl;
	for (int i = 1; i < n; ++i) {
		for (int j = 1; j < m; ++j) {
			S[i][j] = min( S[i-1][j], S[i][j-1] ) + M[i][j]; 
		}
	}

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cout << S[i][j] << " ";
		}
		cout << endl; 
	}

	int i = n-1, j = m-1;
	while (i != 0 and j != 0) {
		cout << "(" << i << ", " << j << ")" << endl;
		if (S[i-1][j] < S[i][j-1]) {
			--i;
		} else {
			--j;
		}
	}

	while (i != 0) {
		cout << "(" << i << ", " << j << ")" << endl;
		--i;
	}

	while (j != 0) {
		cout << "(" << i << ", " << j << ")" << endl;
		--j;
	}

	cout << "(" << i << ", " << j << ")" << endl;
}
