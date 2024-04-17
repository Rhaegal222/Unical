package esercizio2;

import java.util.Scanner;

public class contaCifrev2 {
    public static void main (String[] args) {
        Scanner in=new Scanner(System.in);
        String numero;
        int i, cont = 0;
        System.out.print("Inserisci la stringa: ");
        numero = in.nextLine();

        for(i = numero.indexOf(numero); i < numero.length(); i++) {
            cont++;
        }

        System.out.println(cont);
        System.out.println(numero.length());

    }
}
