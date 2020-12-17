package com.oliverf.codewars;

import java.util.Arrays;

class Dinglemouse {
    private static final String ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789\n";
    
    public static String[] flapDisplay(final String[] lines, final int[][] rotors) {
        
        String[] ans = lines;
        
        for (int i = 0; i < rotors.length; i++) {
            for (int j = 0; j < ans[i].toCharArray().length; j++) {
                System.out.println(ans[i]);
                ans[i] = ans[i].substring(0,j) + (char) ((int) ans[i].charAt(j) + rotors[i][j]) + ans[i].substring(j);
                System.out.println(ans[i]);
            }
        }
        
        return ans;
    }
    
    public static void main(String[] args) {
        System.out.println(Arrays.toString(Dinglemouse.flapDisplay(new String[]{"CAT"}, new int[][]{{1, 13, 27}})));
    }
}
