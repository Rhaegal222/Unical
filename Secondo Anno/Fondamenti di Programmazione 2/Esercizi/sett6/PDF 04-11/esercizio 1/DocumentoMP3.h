#ifndef documentoMP3_h
#define documentoMP3_h
#include "Documento.h"

class DocumentoMP3 : public Documento {
protected:
    float durata;
public:
    DocumentoMP3() {}

    DocumentoMP3(string proprietario, string descrizione, int dimensioneFile, float durata) :
        Documento{ proprietario, descrizione, dimensioneFile },
        durata{ durata } {}

    DocumentoMP3(const DocumentoMP3& doc) :
        Documento{ doc.proprietario, doc.descrizione, doc.dimensioneFile },
        durata{ doc.durata } {}

    float getDurata() const { return durata; }
    void setDurata(float durata) { this->durata = durata; }
};
#endif