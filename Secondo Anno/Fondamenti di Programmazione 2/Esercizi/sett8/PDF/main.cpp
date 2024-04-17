#include "functions.cpp"

int main(){
    //UNO.insFiglio(SIN, SETTE);                    /*                        */    //2.F
    //UNO.insFiglio(DES, NOVE);                     /*           1            */    //3.V (k=32)
    //NOVE.insFiglio(DES, NOVEB);                   /*         /    \         */    //4.F
    //NOVEB.insFiglio(SIN, CINQUEB);                /*        7      9        */    //5.-
    //SETTE.insFiglio(SIN, DUE);                    /*       / \      \       */    //6.5703
    //SETTE.insFiglio(DES, SEI);                    /*      2   6      9      */    //7.F (k=19)
    //SEI.insFiglio(SIN, CINQUE);                   /*         / \    /       */    //8.F (k=20)
    //SEI.insFiglio(DES, UNDICI);                   /*        5   11 5        */    //9.F
    
    //DIECI.insFiglio(SIN, NOVE);                   /*  1.T 2.kmax=32 3.T 4.T */    //2.V
    //DIECI.insFiglio(DES, SETTE);                  /*            10          */    //3.V (k=32) 
    //NOVE.insFiglio(SIN, OTTO);                    /*          /    \        */    //4.V
    //NOVE.insFiglio(DES, SEI);                     /*         9      7       */    //5.-
    //OTTO.insFiglio(SIN, CINQUE);                  /*        / \    /        */    //6.33805
    //OTTO.insFiglio(DES, TRE);                     /*       8   6  4         */    //7.V (k=19)
    //SETTE.insFiglio(SIN, QUATTRO);                /*      / \      \        */    //8.F (k=20)
    //QUATTRO.insFiglio(DES, UNO);                  /*     5   3      1       */    //9.F

    //DIECI.insFiglio(SIN, SETTE);                  /*                        */    //2.F
    //DIECI.insFiglio(DES, TRE);                    /*            10          */    //3.V (k=32)
    //SETTE.insFiglio(SIN, NOVE);                   /*          /    \        */    //4.F
    //SETTE.insFiglio(DES, QUATTRO);                /*         7      3       */    //5.-
    //TRE.insFiglio(SIN, MTRE);                     /*        / \    /        */    //6.32934
    //MTRE.insFiglio(DES, MUNO);                    /*       9   4  -3        */    //7.V (k=19)
    //NOVE.insFiglio(SIN, SEI);                     /*      / \       \       */    //8.V (k=20)
    //NOVE.insFiglio(DES, CINQUE);                  /*     6   5      -1      */    //9.F

    //DIECI.insFiglio(SIN, SETTE);                  /*                        */    //2.F
    //DIECI.insFiglio(DES, TRE);                    /*            10          */    //3.V (k=32)
    //SETTE.insFiglio(SIN, NOVE);                   /*          /    \        */    //4.F
    //SETTE.insFiglio(DES, MQUATTRO);               /*         7      3       */    //5.-
    //TRE.insFiglio(SIN, MTRE);                     /*        / \    /        */    //6.32926
    //MTRE.insFiglio(DES, MUNO);                    /*       9   -4  -3       */    //7.V (k=19)
    //NOVE.insFiglio(SIN, SEI);                     /*      / \       \       */    //8.V (k=20)
    //NOVE.insFiglio(DES, CINQUE);                  /*     6   5       -1     */    //9.V

    //A.insFiglio(SIN, B);                          /*             A          */    //2.-
    //A.insFiglio(DES, C);                          /*           /   \        */    //3.-
    //B.insFiglio(SIN, E);                          /*          B     C       */    //4.-
    //B.insFiglio(DES, D);                          /*         / \    /       */    //5.V
    //C.insFiglio(SIN, F);                          /*        E   D  F        */    //6.-
    //F.insFiglio(DES, I);                          /*       / \      \       */    //7.-
    //E.insFiglio(SIN, G);                          /*      G   H      I      */    //8.-
    //E.insFiglio(DES, H);                          /*                /       */    //9.-
    //I.insFiglio(DES, O);                          /*               O        */  

    //A.insFiglio(SIN, B);                          /*             A          */    //2.-
    //A.insFiglio(DES, C);                          /*           /   \        */    //3.-
    //B.insFiglio(SIN, E);                          /*          B     C       */    //4.-
    //B.insFiglio(DES, D);                          /*         / \    /       */    //5.F
    //D.insFiglio(DES, J);                          /*        E   D  F        */    //6.-
    //C.insFiglio(SIN, F);                          /*       / \   \  \       */    //7.-
    //F.insFiglio(DES, I);                          /*      G   H   J  I      */    //8.-
    //E.insFiglio(SIN, G);                          /*                 /      */    //9.-
    //E.insFiglio(DES, H);                          /*                O       */
    //I.insFiglio(SIN, O);                          /*                        */

    //A.insFiglio(SIN, B);                          /*             A          */    //2.-
    //A.insFiglio(DES, C);                          /*           /   \        */    //3.-
    //B.insFiglio(SIN, E);                          /*          B     C       */    //4.-
    //B.insFiglio(DES, I);                          /*         / \    /       */    //5.V
    //C.insFiglio(SIN, G);                          /*        E   I  G        */    //6.-
    //E.insFiglio(SIN, F);                          /*       / \   \  \       */    //7.-
    //E.insFiglio(DES, H);                          /*      F   H   J  D      */    //8.-
    //I.insFiglio(DES, J);                          /*                 /      */    //9.-
    //G.insFiglio(DES, D);                          /*                O       */
    //D.insFiglio(SIN, O);                          /*                        */
    
    /*esercizio 1*/
    stampaAlbero(DIECI, 5);
        
    /*esercizio 2*/
    cout << "Is heap: ";
    if(isHeap(DIECI)) cout << "Condizioni rispettate!" << endl;
    else cout << "Condizioni NON rispettate!" << endl;

    /*esercizio 3*/
    int k = 32;
    cout << "Ogni percorso radice foglia: ";
    if(ogniPercorsoRadiceFoglia(DIECI, 0, k)) cout << "Condizioni rispettate!" << " (k=" << k << ")" << endl;
    else cout << "Condizioni NON rispettate!" << "(k=" << k << ")" << endl;

    /*esercizio 4*/
    cout << "Pari e dispari: ";
    if(pariEDispari(DIECI, 0)) cout << "Condizioni rispettate!" << endl;
    else cout << "Condizioni NON rispettate!" << endl;

    /*esercizio 5*/
    cout << "Vocali e consonanti: ";
    if(vocaliEConsonanti(A, 0)) cout << "Condizioni rispettate!" << endl;
    else cout << "Condizioni NON rispettate!" << endl;

    /*esercizio 6*/
    int sum = 0;
    cout << "Somma: " << sommaPath(DIECI, sum, 0) << endl;

    /*Esercizio 7*/
    k = 19;
    cout << "Somma livello: "; 
    if(sommaLivello(DIECI, k)) cout << "Condizioni rispettate! " << "(k=" << k << ")" << endl;
    else cout << "Condizioni NON rispettate!" << "(k=" << k << ")" << endl;
    //for(auto i : levels) cout << i << " ";
    //cout << endl;

    /*Esercizio 8*/
    k = 20;
    cout << "Somma livelli adiacenti: ";
    if(sommaLivelliAdiacenti(DIECI, k)) cout << "Condizioni rispettate!" << "(k=" << k << ")" << endl;
    else cout << "Condizioni NON rispettate!" << "(k=" << k << ")" << endl;
    //for(auto i : levels2) cout << i << " ";
    //cout << endl;

    /*Esercizio 9*/
    cout << "Foglie positive = negative: ";
    int diff = 0;
    if(fogliePosEqfoglieNeg(DIECI, diff)) cout << "Condizioni rispettate!" << endl;
    else cout << "Condizioni NON rispettate!" << endl;

    /*Esercizio 10*/
    vector<int> vect{6, 1, 3, 4, 5, 2, 7};
    vecToAlbero(vect);
}