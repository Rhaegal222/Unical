package esercizio4;

import java.util.Scanner;

public class numeriPrimi
{
    public static void main (String[] args)
    {
        Scanner in = new Scanner(System.in);
        int numero1, numero2, cont = 0;
        System.out.print("Inserisci il primo numero: ");
        numero1 = in.nextInt();
        System.out.print("Inserisci il secondo numero: ");
        numero2 = in.nextInt();
        in.close();

        for (int i = numero1; i <= numero2; i++)
        {
            for(int j=1; j<=i; j++)
            {
                if(i%j==0)
                {
                    cont++;
                }
            }
            if((cont<=2)&&(i != 1))
            {
                System.out.print(i+" ");
            }
            cont = 0;
        }
    }
}
