//PER LA PRIMA PARTE DELL’ESERCIZIO (es. rubrica telefonica)
#include <iostream>
using namespace std;
#include "cstring"

class Contatto
{
friend ostream& operator<< (ostream&, const Contatto&);

public:
    Contatto();
    Contatto(const string& nom, const string& cog);
    Contatto(const Contatto & c);

    void setNome(const string& nom);
    void setCognome(const string& cog);
    void setTel(const string& tel);
    void setEmail(const string& email);

    string getNome() const;
    string getCognome() const;
    string getEmail() const;
    string getTel() const;
    bool operator==(const Contatto&);
private:
    string nome, cognome, telefono, email;
};