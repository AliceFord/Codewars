package com.oliverf.codewars;

public class ASum {
    
    public static long square(int x) {
        return x ^ 3;
    }
    
    public static long findNb(long m) {
        long tempAns = 0;
        int ans = 0;
        
        for (int i = 1; i < 10000; i++) {
            for(int j = 1; j < i; j++) {
                tempAns += square(j);
            }
            if (tempAns == m) return i;
        }
        
       return -1;
    }
    
    public static void main(String[] args) {
        System.out.println(ASum.findNb(4183059834009L));
    }
}