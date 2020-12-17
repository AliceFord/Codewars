package com.oliverf.codewars;

public class BraceChecker {

    public static boolean isValid(String braces) {
        int b1 = 0;
        int b2 = 0;
        int b3 = 0;

        for (char character : braces.toCharArray()) {
            if (character == '(') b1 += 1;
            else if (character == ')') b1 -= 1;
            else if (character == '[') b2 += 1;
            else if (character == ']') b2 -= 1;
            else if (character == '{') b3 += 1;
            else b3 -= 1;
        }
       return (b1 == 0) && (b2 == 0) && (b3 == 0);
    }

    public static void main(String[] args) {
        System.out.println(BraceChecker.isValid("{}{}{}{}[[[]]]()"));
    }
}