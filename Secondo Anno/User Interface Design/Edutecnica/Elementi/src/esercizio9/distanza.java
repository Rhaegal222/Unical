package esercizio9;

import java.util.Scanner;

public class distanza {
    public static void main (String[] args)
    {
        Scanner in = new Scanner(System.in);
        double x1, x2, y1, y2, d;

        System.out.print("ins. x1: ");
        x1 = in.nextDouble();
        System.out.print("ins. y1: ");
        y1 = in.nextDouble();
        System.out.print("ins. x2: ");
        x2 = in.nextDouble();
        System.out.print("ins. y2: ");
        y2 = in.nextDouble();
        in.close();

        d=Math.sqrt(Math.pow(x1-x2,2)+Math.pow(y1-y2,2));

        System.out.println("La distanza è: "+d);
    }
}
