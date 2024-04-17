package esercizio7;

import java.util.Scanner;

public class maxMin
{
    public static void main (String[] args)
    {
        Scanner in = new Scanner(System.in);
        int numero, massimo , minimo;

        System.out.print("ins.numero: ");
        numero = in.nextInt();
        massimo=minimo=numero;

        do {
            System.out.print("ins.numero: ");
            numero = in.nextInt();
            if(numero>massimo) massimo = numero;
            if(numero<minimo && numero!=0) minimo = numero;
        }while(numero!=0);
        in.close();

        System.out.println("Numero massimo: "+massimo);
        System.out.println("Numero minimo: "+minimo);
    }
}
