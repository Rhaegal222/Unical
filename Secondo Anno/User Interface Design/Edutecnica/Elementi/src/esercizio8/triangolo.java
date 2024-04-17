package esercizio8;

import java.util.Scanner;

public class triangolo {
    public static void main (String[] args)
    {
        Scanner in = new Scanner(System.in);
        int a, b, c;

        System.out.print("ins. il lato a: ");
        a = in.nextInt();
        System.out.print("ins. il lato b: ");
        b = in.nextInt();
        System.out.print("ins. il lato c: ");
        c = in.nextInt();
        in.close();

        if(a<b+c && b<a+c && c<a+b) System.out.println("Il triangolo esiste");
        else System.out.println("Il triangolo NON esiste");
    }

}
