package com.oliverf.codewars;

import java.util.Arrays;

public class Hamming {
    public static long hamming(int n) {
        long[] hammingNums = new long[5000];
        
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                for (int k = 0; k < 100; k++) {
                    for (int l = 0; l < hammingNums.length; l++) {
                        double v = Math.pow(2, i) * Math.pow(2, j) * Math.pow(2, k);
                        if (hammingNums[l] != v) {
                            hammingNums[i*j*k*l] = (long) v;
                        }
                    }
                }
            }
        }
        System.out.println(Arrays.toString(hammingNums));
        return -1;
    }
    
    public static void main(String[] args) {
        hamming(10);
    }
}