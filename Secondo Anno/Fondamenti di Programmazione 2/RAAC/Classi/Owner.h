#ifndef __OWNER__H__
#define __OWNER__H__

#include <string>
#include <iostream>
using namespace std;

class Owner{
    int id;
    string name, surname;
    public:
        Owner(int id, string name, string surname) : id(id), name(name), surname(surname){};

        Owner(const Owner& Owner){};

        int get_id(){return id;}
        string get_name(){return name;}
        string get_surname(){return surname;}

        void set_id(int id){this->id=id;}
        void set_name(string name){this->name=name;}
        void set_surname(string surname){this->surname=surname;}

        friend ostream& operator<<(ostream& o, const Owner& own){
		o << own.id << "\t" << own.name << "\t" << own.surname << "\t";
		return o;
	    }
};
#endif  //!__OWNER__H__