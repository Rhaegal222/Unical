#ifndef DOCUMENTO_H
#define DOCUMENTO_H 
#include <string.h>
#include <iostream>

using namespace std;

class Documento{
    protected:
        string proprietario;
        string descrizione;
        int dimensioneFile;
    
    public:
        Documento(){};
        Documento(string proprietario, string descrizione, int dimensioneFile):
            proprietario{proprietario},
            descrizione{descrizione},
            dimensioneFile{dimensioneFile}
        {}

        Documento(const Documento& doc):
            proprietario{doc.proprietario},
            descrizione{doc.descrizione},
            dimensioneFile{doc.dimensioneFile}
        {}

        string getProprietario() const {return proprietario;}
        string getDescrizione() const {return descrizione;}
        int getDimensioneFile() const {return dimensioneFile;}

        void setProprietario(string proprietario){this->proprietario = proprietario;}
        void setDescrizione(string descrizione){this->descrizione = descrizione;}
        void setDimenzioneFile(int dimensioneFile){this->dimensioneFile = dimensioneFile;}

};
#endif