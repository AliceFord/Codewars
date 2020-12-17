package com.oliverf.codewars;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class GapInPrimes {
    
    public static long[] gap(int g, long m, long n) {
        List<Integer> primes = IntStream.rangeClosed((int) m, (int) n)
                .filter(GapInPrimes::isPrime).boxed()
                .collect(Collectors.toList());
        for (Integer i : primes){
            System.out.println(i);
        };
        return new long[]{};
    }
    
    private static boolean isPrime(int number) {
        return IntStream.rangeClosed(2, (int) (Math.sqrt(number)))
                .filter(n -> (n & 0X1) != 0)
                .allMatch(n -> number % n != 0);
    }
    
    public static void main(String[] args) {
        System.out.println(Arrays.toString(GapInPrimes.gap(2, 2, 10)));
    }
}