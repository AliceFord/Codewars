package com.oliverf.codewars;

import java.util.Arrays;

public class StripComments {
    
    public static String stripComments(String text, String[] commentSymbols) {
        StringBuilder ans = new StringBuilder();
        for (String line : text.split("\\r?\\n")) {
            boolean isSymbol = false;
            for (String symbol : commentSymbols) {
                if (line.contains(symbol)) {
                    ans.append(line, 0, line.indexOf(symbol));
                    if (ans.charAt(ans.length()-1) == ' ') ans.replace(0, ans.length(), ans.substring(0, ans.length() - 1));
                    ans.append('\n');
                    isSymbol = true;
                }
            }
            if (!isSymbol) ans.append(line).append("\n");
        }
        return ans.charAt(ans.length()-1) == '\n' ? ans.replace(0, ans.length(), ans.substring(0, ans.length() - 1)).toString() : ans.toString();
    }
    
    public static void main(String[] args) {
        System.out.println(StripComments.stripComments("apples, pears # and bananas\ngrapes\nbananas !apples", new String[] { "#", "!" }));
    }
}
