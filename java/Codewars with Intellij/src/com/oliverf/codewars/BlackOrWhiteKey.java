package com.oliverf.codewars;

import java.util.Arrays;

public class BlackOrWhiteKey {
    public static String blackOrWhiteKey(int keyPressCount) {
        return Arrays.stream(new int[]{2, 5, 7, 10, 12}).anyMatch(i -> i == keyPressCount % 88 % 12) ? "black" : "white";
    }
    
    public static void main(String[] args) {
        System.out.println(BlackOrWhiteKey.blackOrWhiteKey(5));
    }
}
