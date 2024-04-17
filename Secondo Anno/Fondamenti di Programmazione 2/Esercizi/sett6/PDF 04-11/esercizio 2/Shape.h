#ifndef SHAPE_H
#define SHAPE_H

#define PI 3.141592653
#include <string>

using namespace std;

class Shape{
    
    public:
    /* Restituisce il perimetro della figura */
    virtual double perimeter() const = 0;
    
    /* Restituisce l'area della figura */
    virtual double area() const = 0;

    virtual string representation() const = 0;

    friend ostream& operator<<(ostream& o, const Shape& a){
    o << a.representation();
    return o;
    }
};

class Circle: public Shape{
    public:
	// r: raggio
	Circle(double r): r(r){}
	virtual double perimeter() const override {
		return 2 * PI * r;
	}
	virtual double area() const override {
		return PI * r * r;
	}
	virtual string representation() const override {
		return "Circle(r=" + to_string(r) + ")";
	}
	const double r;
};

class Rectangle: public Shape{
    public:
	//a: lato, b: lato
	Rectangle(double a, double b): a(a), b(b) {}

	virtual double perimeter() const override{
		return (a+b)*2;
	}
	virtual double area() const override{
		return a*b;
	}
	virtual string representation() const override{
		return "Rectangle(a=" + to_string(a) + ", b=" + to_string(b) + ")";
	}
	const double a;
	const double b;
};

class Square: public Rectangle{
    public:
	//a: lato
	Square(double a): Rectangle(a,a){}
	virtual string representation() const override{
		return "Square(a=" + to_string(a) + ")";
	}
};
#endif