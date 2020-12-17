package com.oliverf.codewars;

public class TenMinWalk {
    public static boolean isValid(char[] walk) {
        if (walk.length != 10) return false;
        int countNS = 0;
        int countEW = 0;
        for (char character : walk) {
            if (character == 'n') countNS += 1;
            else if (character == 's') countNS -= 1;
            else if (character == 'e') countEW += 1;
            else countEW -= 1;
        }
        return countNS == 0 && countEW == 0;
    }

    public static void main(String[] args) {
        System.out.println(TenMinWalk.isValid(new char[] {'n','s','n','s','n','s','n','s','w','s'}));
    }
}