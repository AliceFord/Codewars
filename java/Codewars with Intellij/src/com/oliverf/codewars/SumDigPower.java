package com.oliverf.codewars;

import java.util.ArrayList;
import java.util.List;

class SumDigPower {
    
    public static List<Long> sumDigPow(long a, long b) {
        List<Long> ans = new ArrayList<>();
        
        while (a < b) {
            String temp = Integer.toString((int) a);
            int tempAns = 0;
            for (int i = 1; i <= String.valueOf(a).length(); i++) {
                tempAns += Math.pow(temp.charAt(i - 1) - '0', i);
            }
            if (tempAns == a) ans.add(a);
            a++;
        }
        
        return ans;
    }
    
    public static void main(String[] args) {
        System.out.println(SumDigPower.sumDigPow(1, 10));
    }
}