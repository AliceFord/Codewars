package com.oliverf.codewars;

public class Maskify {
    public static String maskify(String str) {
    	String newString = "";
        if (str.length() - 4 >= 0) {
        	for (int i = 0; i < str.length() - 4; i++) {
        		newString += "#";
        	}
        	return newString + str.substring(str.length() - 4);
        } else {
        	return str;
        }

    }
    
    public static void main(String[] args) {
    	
    	System.out.println(Maskify.maskify("Yusmsas"));
    }
}