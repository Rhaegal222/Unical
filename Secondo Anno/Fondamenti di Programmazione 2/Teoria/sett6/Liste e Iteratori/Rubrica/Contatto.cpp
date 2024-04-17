/*
Esempi d’uso di liste con classi generiche (es. rubrica) ed iteratori su liste
*/
#include <iostream>
#include "../ListaT.h"
#include "../Iterator.h"
#include "Contatto.h"

using namespace std;
#include "cstring"

Contatto::Contatto():
        nome(""), cognome(""), telefono(""), email("") {}

Contatto::Contatto(const string& nom, const string& cog)  :
        nome(nom), cognome(cog), telefono(""), email("") {}

Contatto::Contatto(const Contatto& c) :
        nome(c.nome), cognome(c.cognome), telefono(c.telefono), email(c.email) {}

void Contatto::setNome(const string & nom){nome = nom;}
void Contatto::setCognome(const string & cog){cognome = cog;}
void Contatto::setTel(const string & tel){telefono = tel;}
void Contatto::setEmail(const string & email){this->email = email;}

string Contatto::getNome() const{return nome;}
string Contatto::getCognome() const{return cognome;}
string Contatto::getEmail() const{return email;}
string Contatto::getTel() const{return telefono;}

bool Contatto::operator==(const Contatto& c)
{
    return nome==c.nome &&
           cognome == c.cognome &&
           telefono== c.telefono &&
           email == c.email;
}

ostream& operator<< (ostream& o, const Contatto & c)
{
        o << c.getNome() << " - ";
        o << c.getCognome() << " - ";
        o << c.getEmail() << " - ";
        o << c.getTel() << endl;
        return o;
}

//FUZIONE DI UTILITA’ PER L’ESEMPIO
bool cerca(List<Contatto> &L, const string & s)
{
   Node<Contatto> * p = L.front();
   while (p!=0)
   {
       if(p->getValue().getCognome() == s)

                      return true;


       p=p->getNextNode();
   }
   return false;

}