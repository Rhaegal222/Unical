#include <iostream>
#include "shape.h"
#include <vector>
#include <algorithm>
using namespace std; 

int main() {
	vector<Shape*> shapes;
	Rectangle r(3.0, 4.0);
	Square s(8.0); 
	Circle c(3.0); 
	shapes.push_back(&r);
	shapes.push_back(&s);
	shapes.push_back(&c);

	struct {
		double operator()(Shape* s1, Shape* s2) {
			double d1 = s1->area() / s1->perimeter();
			double d2 = s2->area() / s2->perimeter();
			return d1 < d2;
		}
	} density_functor;

	// sort: dalla libreria <algorithm>, syntax(iterator, iterator, comparison functor)
	sort(shapes.begin(), shapes.end(), density_functor); 

	int k = 3;
	auto it = shapes.rbegin(); 
	while (k--) {
		cout << **it << endl; 
		it++;
	}
	return 0; 
}
