package com.oliverf.codewars;

class RowSumOddNumbers {
    public static int rowSumOddNumbers(int n) {
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            ans += 2 * n - 1 + i;
        }

        return ans;
    }

    public static void main(String[] args) {
        System.out.println(RowSumOddNumbers.rowSumOddNumbers(2));
    }
}