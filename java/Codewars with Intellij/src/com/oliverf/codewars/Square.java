package com.oliverf.codewars;

public class Square {
    public static boolean isSquare(int n) {
        double sqr = Math.sqrt(n);
        return ((sqr - Math.floor(sqr)) == 0);
    }

    public static void main(String[] args) {
        System.out.println(Square.isSquare(2500));
    }
}