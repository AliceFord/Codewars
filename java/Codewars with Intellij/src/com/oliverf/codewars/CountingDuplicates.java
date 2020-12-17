package com.oliverf.codewars;

public class CountingDuplicates {
    public static int duplicateCount(String text) {
        text = text.toLowerCase();
        int[] nums = new int[128];
        int ans = 0;
        for (int i = 0; i < text.length(); i++) {
            if (nums[text.charAt(i)] == 0) {
                nums[text.charAt(i)] = 1;
            } else if (nums[text.charAt(i)] == 1){
                nums[text.charAt(i)] = 2;
                ans += 1;
            }
        }

        return ans;
    }

    public static void main(String[] args) {
        System.out.println(CountingDuplicates.duplicateCount("iii"));
    }
}