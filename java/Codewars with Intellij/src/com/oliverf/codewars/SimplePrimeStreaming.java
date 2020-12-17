package com.oliverf.codewars;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class SimplePrimeStreaming {
    public static String solve(int a, int b) {
        List<Integer> primes = sieveOfEratosthenes(100000);
        StringBuilder primesString = new StringBuilder();
        for (int i : primes) {
            primesString.append(i);
        }
        return primesString.toString().substring(a, a+b);
    }
    
    public static List<Integer> sieveOfEratosthenes(int n) {
        boolean[] prime = new boolean[n + 1];
        Arrays.fill(prime, true);
        for (int p = 2; p * p <= n; p++) {
            if (prime[p]) {
                for (int i = p * 2; i <= n; i += p)
                    prime[i] = false;
            }
        }
        List<Integer> primeNumbers = new LinkedList<>();
        for (int i = 2; i <= n; i++) {
            if (prime[i]) {
                primeNumbers.add(i);
            }
        }
        return primeNumbers;
    }
    
    public static void main(String[] args) {
        System.out.println(SimplePrimeStreaming.solve(10, 5));
        System.out.println(SimplePrimeStreaming.sieveOfEratosthenes(20000));
    }
}