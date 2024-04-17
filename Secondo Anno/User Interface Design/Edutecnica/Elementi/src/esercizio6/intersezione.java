package esercizio6;

import java.util.Scanner;

public class intersezione
{
    public static void main (String[] args)
    {
        Scanner in=new Scanner(System.in);
        double a,b,c,d, j;
        boolean intersecanti = true;

        System.out.print("ins.a: ");
        a=in.nextDouble();
        System.out.print("ins.b: ");
        b=in.nextDouble();
        System.out.print("ins.c: ");
        c=in.nextDouble();
        System.out.print("ins.d: ");
        d=in.nextDouble();
        in.close();

        if (a>b)
        {
          j = b;
          b = a;
          a = j;
        }
        if (c>d)
        {
            j = d;
            d = c;
            c = j;
        }

        if(b<c || d<a) intersecanti = false;
        if(intersecanti) System.out.println("Hanno degli elementi in comune");
        else System.out.println("Non hanno nessun elemento in comune");

    }//fine main
}//fine class

