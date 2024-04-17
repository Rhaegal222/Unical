#ifndef __PRODOTTO__H__
#define __PRODOTTO__H__
#include <string>
using namespace std;
class Prodotto{
private:
    string nome;
    double prezzo;
public:
    Prodotto(string nome, double prezzo){this->nome=nome; this->prezzo=prezzo;}
    Prodotto(const Prodotto& prodotto){this->nome=prodotto.get_nome(); this->prezzo=prodotto.get_prezzo();}
    string get_nome() const{return this->nome;}
    double get_prezzo() const{return this->prezzo;}
    bool operator==(const Prodotto& prodotto)const{
        return(prodotto.nome==nome && prodotto.prezzo == prezzo);
    }

};
#endif  //!__PRODOTTO__H__