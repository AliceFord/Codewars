package com.oliverf.codewars;

public class NumberFun {
    public static long findNextSquare(long sq) {
        //double sqr = Math.sqrt(sq);
        //return ((sqr - Math.floor(sqr)) == 0);
        int iterator = 0;
        while (true) {
            double sqr = Math.sqrt(sq + iterator);
            if ((sqr - Math.floor(sqr)) == 0) {
                return (long) ( sqr * sqr);
            }
            iterator++;
        }
    }
    public static void main(String[] args) {
        System.out.println(NumberFun.findNextSquare(142));
    }
}