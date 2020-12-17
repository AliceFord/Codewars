package com.oliverf.codewars;

import java.util.Arrays;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;
import java.util.Random;

// TODO: Replace examples and use TDD by writing your own tests

class SolutionTest {
    @Test
    public void basicTests() {
        assertEquals(Opposite.isOpposite("ab", "AB"), true);
        assertEquals(Opposite.isOpposite("aB", "Ab"), true);
        assertEquals(Opposite.isOpposite("aBcd", "AbCD"), true);
        assertEquals(Opposite.isOpposite("AB", "Ab"), false);
        assertEquals(Opposite.isOpposite("", ""), false);
    }
    @Test
    public void randomTests() {
        Random rand = new Random();
        for (int i = 0; i < 100; i++) {
            ;
        }
    }
}



public class Opposite {
    
    public static boolean isOpposite (String s1, String s2) {
        char[] s1Chars = s1.toCharArray();
        for(int i = 0; i < s1.length(); i++) {
            s1Chars[i] = Character.isUpperCase(s1Chars[i]) ? Character.toLowerCase(s1Chars[i]) : Character.toUpperCase(s1Chars[i]);
        }
        return Arrays.equals(s1Chars, s2.toCharArray()) && !(s1.equals(""));
    }
    
    public static void main(String[] args) {
        System.out.println(Opposite.isOpposite("ab", "AB"));
    }
    
}