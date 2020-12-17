package com.oliverf.codewars;

import java.util.Arrays;

public class Tortoise {
    public static int[] race(int v1, int v2, double g) {
        if (v1 >= v2) return null;
        int time = 0;
        while (true) {
            System.out.println(v2 / 3600d);
            g += v1 / 3600d;
            g -= v2 / 3600d;
            time += 1;
            if (g <= 0) return new int[] {time};
        }
    }
    
    public static void main(String[] args) {
        System.out.println(Arrays.toString(Tortoise.race(720, 850, 70)));
    }
}