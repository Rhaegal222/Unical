package esercizio3;

import java.util.Scanner;

public class cercaDivisori {
    public static void main (String[] args) {
        Scanner in = new Scanner(System.in);
        int numero, i, cont = 0;
        System.out.print("Inserisci il numero: ");
        numero = in.nextInt();

        for (i = 1; i <= numero; i++) {
            if (numero % i == 0) {
                System.out.print(i+" ");
                cont++;
            }
        }
        System.out.println();
        System.out.println(cont);
    }
}
