package com.oliverf.codewars;

public class FindOutlier {
    static int find(int[] integers) {
        int isEven;
        if (integers[0] % 2 == integers[1] % 2) isEven = integers[0] % 2;
        else if (integers[0] % 2 == integers[2] % 2) return integers[1];
        else return integers[0];
        for (int i = 2; i < integers.length; i++) {
            if (integers[i] % 2 != isEven) return integers[i];
        }
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(FindOutlier.find(new int[] {2,6,8,-10,3}));
    }
}