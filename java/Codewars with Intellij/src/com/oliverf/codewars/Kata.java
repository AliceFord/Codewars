package com.oliverf.codewars;

import java.security.KeyPairGenerator;
import java.util.Arrays;

public class Kata {
    public static int findEvenIndex(int[] arr) {
        int[] tempArrNum = null;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length - j; j++) {
                tempArrNum[j] += arr[j + 1];
            }

            if (arr[i] == tempArrNum[i]) {
                return i;
            }
        }

        return -1;
    }

    public static String expandedForm(int num)
    {
        // int to int[], *10, continue
        int j = 0;
        int len = Integer.toString(num).length();
        int[] arr = new int[len];
        while (num!=0) {
            arr[len-j-1] = num%10 * (10 * j);
            num /= 10;
            j++;
        }
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < len; i++) {
            ans.append(arr[i]);
            ans.append(" + ");
        }
        return ans.toString();
    }

    /*
    Iterate over string one, letter by letter. Flip every occurance on a per letter basis.
    Repeat for second string.
    Concatinate!
    */

    public static char flipStringCaps(char a) {
        if (a > 64 && a < 91) return (char) (a + 32);
        else return (char) (a - 32);
    }

    public static String workOnStrings(String a, String b) {

        for (char charA : a.toCharArray()) {
            for (char charB : b.toCharArray()) {
                if (charA % 32 == charB % 32) b = b.replace(charB, flipStringCaps(charB));
            }
        }

        for (char charB : b.toCharArray()) {
            for (char charA : a.toCharArray()) {
                if (charA % 32 == charB % 32) a = a.replace(charA, flipStringCaps(charA));
            }
        }

        return a + b;
    }


    public static char findMissingLetter(char[] array)
    {
        char lastChar = array[0];
        for (char character : array) {
            if (character != lastChar + 1) return (char) (lastChar + 1);
            lastChar = character;
        }
        return ' ';
    }
    
    public static int[] sortArray(int[] array) {
        int[] oddArr = new int[array.length];
        for (int i = 0; i < array.length; i++) {
            if (array[i] % 2 == 1) oddArr[i] = array[i];
        }
        Arrays.sort(oddArr);
        int firstNum = 0;
        for (int value : oddArr) {
            if (value == 0) firstNum += 1;
            else break;
        }
        for (int i = 0; i < array.length; i++) {
            if (array[i] % 2 == 1) array[i] = oddArr[firstNum];
            firstNum++;
        }
        return array;
    }



    public static void main(String[] args) {
        //System.out.println(Kata.findEvenIndex(new int[] {1,2,3,4,3,2,1}));
        //System.out.println(Kata.expandedForm(1252));
        //System.out.println(Kata.workOnStrings("abc", "abc"));
        //System.out.println(Kata.findMissingLetter(new char[] { 'O','Q','R','S' }));
        System.out.println(Arrays.toString(Kata.sortArray(new int[]{ 5, 3, 2, 8, 1, 4 })));
    }
}