import Es1.Magazzino;
import Es1.Prodotto;

import java.util.Scanner;

public class Main {
    public static void printMenu(){
        System.out.println("Scegli cosa fare \n" +
                "1 - Aggiungi prodotto \n" +
                "2 - Rimuovi prodotto \n" +
                "3 - Ricerca per marca \n" +
                "4 - Ricerca per modello \n" +
                "5 - Ricerca per anno di produzione \n" +
                "6 - Ordina per prezzo crescente \n" +
                "7 - Ordina per prezzo decrescente \n" +
                "8 - Stampa tutti i prodotti \n" +
                "9 - Stampa il menu \n" +
                "0 - Termina il programma");
    }
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        Magazzino store = new Magazzino();

        Prodotto primo = new Prodotto("000","Mela","Melinda","Fuji",2023,1.49);
        Prodotto secondo = new Prodotto("001","Mela","Melinda","Golden",2023,1.29);
        Prodotto terzo = new Prodotto("002","Mela","Melinda","Green",2023,1.69);

        store.addProduct(primo); store.addProduct(secondo);store.addProduct(terzo);

        byte x= 1; byte t;
        printMenu();
        while(true) {
            System.out.print("Voce del menu selezionata: ");
            t = input.nextByte();
            switch (t) {
                case 0:
                    return;
                case 1:
                    store.addProduct();
                    break;
                case 2:
                    System.out.print("Inserisci l'id del prodotto da rimuovere: ");
                    store.removeProduct(input.next());
                    break;
                case 3:
                    System.out.print("Inserisci la marca da cercare: ");
                    store.searchProductByBrand(input.next());
                    break;
                case 4:
                    System.out.print("Inserisci il modello da cercare: ");
                    store.searchProductByModel(input.next());
                    break;
                case 5:
                    System.out.print("Inserisci la anno di produzione da cercare: ");
                    store.searchProductByDot(input.nextInt());
                    break;
                case 6:
                    System.out.println("Ordinato per prezzo ascendente");
                    store.sortByAscendingPrice();
                    System.out.println("Premi 8 per stampare, 9 per visualizzare il menu: ");
                    break;
                case 7:
                    System.out.println("Ordinato per prezzo discendente...");
                    store.sortByDescendingPrice();
                    System.out.println("Premi 8 per stampare, 9 per visualizzare il menu: ");
                    break;
                case 8:
                    System.out.println("Tutti i prodotti: ");
                    store.printAllProducts();
                    break;
                case 9:
                    printMenu();
            }
        }
    }
}