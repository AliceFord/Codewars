package com.oliverf.codewars;
import java.util.Arrays;

public class AreSame {
	
	public static boolean comp(int[] a, int[] b) {
		for (int i = 0; i < a.length; i++) {
			a[i] *= a[i];
		}
		Arrays.sort(a);
		Arrays.sort(b);
		
		if (Arrays.equals(a, b)) return true;
		return false;
	}
	
	public static void main(String[] args) {
		int[] a = new int[]{121, 144, 19, 161, 19, 144, 19, 11};
		int[] b = new int[]{121, 14641, 20736, 361, 25921, 361, 20736, 361};
		System.out.println(AreSame.comp(a, b));
	}
}