package esercizio10;

import java.util.Scanner;

public class numeriUguali {
    public static void main (String[] args)
    {
        Scanner in = new Scanner(System.in);
        double x, y, z;

        System.out.print("ins. x: ");
        x = in.nextDouble();
        System.out.print("ins. y: ");
        y = in.nextDouble();
        System.out.print("ins. z: ");
        z = in.nextDouble();
        in.close();

        if (x==y && x==z) System.out.println("Tutti uguali");
        else if (x==y || x==z || y==z) System.out.println("Uno diverso");
        else System.out.println("Tutti diversi");
    }
}
