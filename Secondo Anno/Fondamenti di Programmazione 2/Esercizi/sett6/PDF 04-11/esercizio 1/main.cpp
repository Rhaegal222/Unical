#include "DocumentoMP3.h"
#include "DocumentoPDF.h"
#include "GestoreDocumenti.h"
#include <iostream>

using namespace std;

int main(){
    Documento* doc = new Documento("Alessio", "Documento.h", 1024);
    DocumentoPDF* pdf = new DocumentoPDF("Gennaro", "Erecizio_308.pdf", 4096, false);
    DocumentoMP3* mp3 = new DocumentoMP3("Adriana", "Quanto ti vorrei by Chiello.mp3", 17054, 170.0);

    GestoreDocumenti Gestore;
    Gestore.aggiungiDocumento(doc);
    Gestore.aggiungiDocumento(pdf);
    Gestore.aggiungiDocumento(mp3);

    Gestore.stampaDocumenti();
    
    Gestore.ordinaDocumenti(1);
    Gestore.stampaDocumenti();

    Gestore.ordinaDocumenti(2);
    Gestore.stampaDocumenti();

    Gestore.ordinaDocumenti(3);
    Gestore.stampaDocumenti();

/*
    cout << doc->getProprietario() << endl;
    cout << doc->getDescrizione() << endl;
    cout << doc->getDimensioneFile() << "Kb\n\n";

    cout << pdf->getProprietario() << endl;
    cout << pdf->getDescrizione() << endl;
    cout << pdf->getDimensioneFile() << "Kb\n";
    if(!pdf->getFirmato()) cout << "NON ";
    cout << "FIRMATO!\n\n";

    cout << mp3->getProprietario() << endl;
    cout << mp3->getDescrizione() << endl;
    cout << mp3->getDimensioneFile() << "Kb\n";
    cout << mp3->getDurata() << "secondi\n\n";
*/

    return 0;
}
