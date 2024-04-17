#include<iostream>
#include<vector>
#include<unordered_map>
#include<algorithm>
#include<cassert>
using namespace std; 

int main() {
	unordered_map<int,vector<int>> graph; 
	int num_nodes, num_edges; 
	cin >> num_nodes >> num_edges;

	vector<int> degrees(num_nodes);
	for (int i = 0; i < num_edges; ++i) {
		int u, v;
		cin >> u >> v; 

		graph[u].push_back(v);
		graph[v].push_back(u);

		degrees[u]++;
		degrees[v]++;
	}

	int num_colors = 1 + *max_element(degrees.begin(), degrees.end());

	vector<int> assignment(num_nodes, -1);
	for (int i = 0; i < num_nodes; ++i) {
		vector<bool> available_colors(num_colors, true);
		for (int v: graph[i]) {
			if (assignment[v] != -1) available_colors[assignment[v]] = false;
		}

		int color = 0;
		while (not available_colors[color]) ++color;
		assignment[i] = color; 
	}

	for (int i = 0; i < num_nodes; ++i) {
		cout << "Node " << i << " has color " << assignment[i] << endl; 
	}

	for (int u = 0; u < num_nodes; ++u) {
		for (int v: graph[u]) {
			assert(assignment[u] != assignment[v]);
		}
	}

	return 0; 
}
