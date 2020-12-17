package com.oliverf.codewars;

import java.util.Arrays;

public class Xbonacci {
    
    public static double[] xbonacci(double[] signature, int n) {
        double[] ans = new double[n];
        
        ans = signature;
        for (int i = signature.length + 1; i < n; i++) {
            for (int j = 0; j < signature.length; j++) {
                ans[i] += signature[i - j];
            }
        }
        
        return ans;
    }
    
    public static void main(String[] args) {
        System.out.println(Arrays.toString(Xbonacci.xbonacci(new double[]{0, 1}, 10)));
    }
}