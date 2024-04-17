package esercizio5;

import java.util.Scanner;

class tassoInteresse {
    public static void main (String[] args) {
        Scanner in=new Scanner(System.in);
        double i,n;
        System.out.print("ins.il tasso:");
        i=in.nextDouble();
        in.close();
        i=i/100;
        n=Math.log(2)/Math.log(1+i);
        System.out.println(n);
    }//fine main
}//fine class
