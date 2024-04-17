#ifndef documentoPDF_h
#define documentoPDF_h 
#include "Documento.h"

class DocumentoPDF : public Documento {
protected:
    bool firmato;
public:
    DocumentoPDF() {}

    DocumentoPDF(string proprietario, string descrizione, int dimensioneFile, bool firmato) :
        Documento{ proprietario, descrizione, dimensioneFile },
        firmato{ firmato } {}

    DocumentoPDF(const DocumentoPDF& doc) :
        Documento{ doc.proprietario, doc.descrizione, doc.dimensioneFile },
        firmato{ doc.firmato } {}

    bool getFirmato() const { return firmato; }
    void setFirmato(bool firmato) { this->firmato = firmato; }
};
#endif