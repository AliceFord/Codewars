package com.oliverf.codewars;

public class Stat {
    
    public static String stat(String strg) {
        if (strg.equals("")) return "";
        int numScores = strg.length() - strg.replaceAll(",", "").length() + 1;
        int[] scores = new int[numScores];
        for (int i = 0; i < numScores; i++) {
            scores[i] = Integer.parseInt(strg.substring(strg.indexOf(','), strg.lastIndexOf(',')));
        }
        
        return "";
    }
}