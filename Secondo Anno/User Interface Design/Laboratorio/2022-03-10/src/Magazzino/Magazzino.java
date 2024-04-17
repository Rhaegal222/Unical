package Magazzino;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Magazzino {

    public static List<Prodotto> prodotti = new ArrayList<Prodotto>();

    public static boolean AddProduct(){

        Scanner cin = new Scanner(System.in);

        System.out.println("Inserisci id prodotto");
        String id = cin.nextLine();

        System.out.println("Inserisci tipo prodotto");
        String type = cin.nextLine();

        System.out.println("Inserisci marca prodotto");
        String brand = cin.nextLine();

        System.out.println("Inserisci modello prodotto");
        String model = cin.nextLine();

        System.out.println("Inserisci anno prodotto");
        Integer year = cin.nextInt();

        System.out.println("Inserisci prezzo prodotto");
        Double price = cin.nextDouble();

        Prodotto p = new Prodotto(id, type, brand, model, year, price);

        prodotti.add(new Prodotto(id, type, brand, model, year, price));

        if (!prodotti.contains(p)) return false;

        prodotti.add(p);

        return true;
    }

    public static void main(String[] args){

        System.out.println("Risultato ricerca per marca:");
        for (Prodotto p: prodotti){
            if (p.getModel().equals(p.brand)) System.out.println(p);
        }

    }
}
