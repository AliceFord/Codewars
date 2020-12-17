package com.oliverf.codewars;

public class BackspacesInString {
    public static String cleanString(String s) {
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '#') {
                if (!ans.toString().equals(""))
                    ans = new StringBuilder(ans.substring(0, ans.length() - 1));
        }
            else
                ans.append(s.charAt(i));
        }
        return ans.toString();
    }
    
    public static void main(String[] args) {
        System.out.println(BackspacesInString.cleanString("a#bc#d"));
    }
}