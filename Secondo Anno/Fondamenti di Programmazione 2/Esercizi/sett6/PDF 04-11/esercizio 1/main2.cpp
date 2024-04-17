#include "DocumentoMP3.h"
#include "DocumentoPDF.h"
#include "GestoreDocumenti.cpp"
#include <iostream>

using std::cout;

int main() {
    GestoreDocumenti lista;

    Documento doc("Alberto", "Preventivo.doc", 1024);
    DocumentoPDF pdf("Mario", "Fattura.pdf", 4096, false);
    DocumentoMP3 mp3("Barbara", "Ricevuta.mp3", 17054, 170.0);

    lista.aggiungiDocumento(&doc);
    lista.aggiungiDocumento(&pdf);
    lista.aggiungiDocumento(&mp3);

    //ordina in base al proprietario

    lista.ordinaDocumenti(1);
    lista.stampaDocumenti();

    //ordina in base alla descrizione

    lista.ordinaDocumenti(2);
    lista.stampaDocumenti();

    //ordina in base alla dimensione del file

    lista.ordinaDocumenti(3);
    lista.stampaDocumenti();

    return 0;
}
