package esercizio1;

import java.util.Scanner;

class sommaInteri {
    public static void main (String[] args) {
        Scanner in=new Scanner(System.in);
        int a,b,i,j,sum=0;
        System.out.print("ins.il primo num: ");
        a=in.nextInt();
        System.out.print("ins.il secondo num: ");
        b=in.nextInt();
        in.close();
        if(a>b){//scambio in modo che b>a
            j=a;
            a=b;
            b=j;
        }
        for(i=a;i<=b;i++)sum+=i;
        System.out.println("somma:"+ sum);
//versione con la formula n*(n+1)/2 i=a*(a+1)/2;
        j=b*(b+1)/2;
//nb. j-i restituisce la somma dei numeri fra b e a+1
        sum=j-i+a;
        System.out.println("somma:"+ sum);
    }//fine main
}//fine class
