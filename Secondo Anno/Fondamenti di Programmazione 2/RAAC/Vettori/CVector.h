#include <iostream>
using namespace std;

class CVector{
private:
    int x, y;
    
public:
    CVector(){};
    CVector(int a, int b):x(a),y(b){};
    
    void set(int a, int b){x = a; y=b;}
    int get(){return x;}

    CVector operator+ (const CVector& param){
        CVector temp;
        temp.x = x + param.x;
        temp.y = y + param.y;
        return temp;
    }
    
    CVector operator= (const CVector& param){
        x = param.x;
        y = param.y;
        return *this;
    }

    friend ostream& operator<<(ostream& o, const CVector& d){
		o << "x: " << d.x << " y: " << d.y;
		return o;
	}
};