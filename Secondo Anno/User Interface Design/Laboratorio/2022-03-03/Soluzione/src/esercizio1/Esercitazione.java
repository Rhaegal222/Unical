package esercizio1;

import java.util.Arrays;
import java.util.Comparator;

public class Esercitazione {
	
	private static void print(String before, int arr[]) {
		System.out.print(before + ":");
		for(int element : arr)
			System.out.print(" " + element);
		System.out.println();
	}
	
	private static boolean isPrime(int element) {
		if(element <= 1)
			return false;
		for(int i = 2; i < element; i++)
			if(element % i == 0)
				return false;			
		return true;
	}

	public static void main(String[] args) {
		int arr[] = {4,6,2,7,2,1,3,4,8,5};
		print("Array", arr);
		
		if(arr.length != 0) {
			int min = arr[0];
			int max = arr[0];
			float sum = 0;
			for(int i = 0; i < arr.length; i++) {
				if(arr[i] < min)
					min = arr[i];
				else if(arr[i] > max)
					max = arr[i];
				sum += arr[i];
			}
			
			System.out.println("Il minimo è: " + min);
			System.out.println("Il massimo è: " + max);		
			System.out.println("La media è: " + sum/arr.length);
		}
		
		Arrays.sort(arr);		
		print("Array ordinato in ordine crescente", arr);
		
		Integer[] tmp = new Integer[arr.length];
		for(int i = 0; i < arr.length; i++)
			tmp[i] = arr[i];
		
		Arrays.sort(tmp, new Comparator<Integer>() {

			@Override
			public int compare(Integer o1, Integer o2) {
				return o2.compareTo(o1);
			}
		});
		for(int i = 0; i < arr.length; i++)
			arr[i] = tmp[i];
		print("Array ordinato in ordine decrescente", arr);
		
		System.out.print("Numeri primi nell'array:");
		for(int element : arr) {
			if(isPrime(element))
				System.out.print(" " + element);
		}
		System.out.println();
		
	}
}
