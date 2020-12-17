package com.oliverf.codewars;

public class SquareDigit {

	  public int squareDigits(int n) {
		String nStr = Integer.toString(n);
		String ans = "";
		for (int i = 0; i < n; i++) {
			ans += Integer.toString(n % 10);
		}
	    return Integer.parseInt(ans);
	  }

	  public static void main(String[] args) {
		  SquareDigit test = null;
		  System.out.println(test.squareDigits(1));
	  }
	}