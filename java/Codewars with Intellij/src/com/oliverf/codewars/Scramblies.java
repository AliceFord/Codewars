package com.oliverf.codewars;

import java.util.Arrays;

public class Scramblies {
    
    public static boolean scramble(String str1, String str2) {
        int[] str1Arr = new int[26];
        Arrays.fill(str1Arr, 0);
        for (int i = 0; i < str1.length(); i++) {
            str1Arr[str1.charAt(i) - 96] += 1;
        }
        
        int[] str2Arr = new int[26];
        Arrays.fill(str2Arr, 0);
        for (int i = 0; i < str2.length(); i++) {
            str2Arr[str2.charAt(i) - 96] += 1;
        }
        
        for (int i = 0; i < str1Arr.length; i++) {
            if (str1Arr[i] < str2Arr[i]) return false;
        }
        // Array for each char x2
        return true;
    }
    
    public static void main(String[] args) {
        System.out.println(Scramblies.scramble("rkqodlw","world"));
    }
}