package com.oliverf.codewars;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class BinaryArrayToNumber {

    public static int ConvertBinaryArrayToInt(List<Integer> binary) {
        int binaryFinal = 0;
        for (int a : binary) {
            binaryFinal = 10 * binaryFinal + a;
        }
        return Integer.parseInt(Integer.toString(binaryFinal), 2);
    }

    public static void main(String[] args) {
        System.out.println(BinaryArrayToNumber.ConvertBinaryArrayToInt(new ArrayList<>(Arrays.asList(0,0,0,1))));
    }
}