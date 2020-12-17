package com.oliverf.codewars;

import java.util.Arrays;

public class Solution {

    public static boolean validatePin(String pin) {
        if (pin.length() != 4 && pin.length() != 6) return false;
        for (char character : pin.toCharArray()) {
            if (character < 48 || character > 57) return false;
        }
        return true;
    }
    
    static String toCamelCase(String s) {
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (s.toCharArray()[i] == '_' || s.toCharArray()[i] == '-') {
                ans.append(s.toUpperCase().toCharArray()[i+1]);
                i += 1;
            } else {
                ans.append(s.toCharArray()[i]);
            }
        }
        
        return ans.toString();
    }
    
    public static String driver(final String[] data) {
        StringBuilder ans = new StringBuilder();
        data[2] += 99999;
        ans.append(data[2].toUpperCase(), 0, 5);
        
        ans.append(data[3].charAt(data[3].length() - 2));
        
        int caseNum;
        switch (data[3].toUpperCase().substring(3, 6)) {
            case "JAN":
                caseNum = 1;
                break;
            case "FEB":
                caseNum = 2;
                break;
            case "MAR":
                caseNum = 3;
                break;
            case "APR":
                caseNum = 4;
                break;
            case "MAY":
                caseNum = 5;
                break;
            case "JUN":
                caseNum = 6;
                break;
            case "JUL":
                caseNum = 7;
                break;
            case "AUG":
                caseNum = 8;
                break;
            case "SEP":
                caseNum = 9;
                break;
            case "OCT":
                caseNum = 10;
                break;
            case "NOV":
                caseNum = 11;
                break;
            case "DEC":
                caseNum = 12;
                break;
            default:
                throw new IllegalStateException("Unexpected value: " + data[3].toUpperCase().substring(3, 6));
        }
    
        //ans.append((data[4].toUpperCase().equals("M") ? caseNum < 10 ? "0" + caseNum : caseNum : caseNum + 50 < 60 ? "0" + caseNum + 50 : caseNum + 50));
        
        ans.append(data[3], 0, 2);
        
        ans.append(data[3].charAt(data[3].length() - 1));
        
        ans.append(data[1].equals("") ? data[0].charAt(0) + "9" : Character.toString(data[0].charAt(0)) + data[1].charAt(0));
        
        ans.append(9);
        
        ans.append("AA");
        
        return ans.toString();
    }
    
    public static int solution(int number) {
        int ans = 0;
        for (int i = 0; i < number; i++) {
            if (i % 3 == 0 || i % 5 == 0) ans += i;
        }
        
        return ans;
    }
    
    public static String camelCase(String str) {
        char[] ans = str.toCharArray();
        if (str.equals("")) return "";
        for (int i = 0; i < str.length(); i++) {
            if (ans[i] == ' ') ans[i + 1] -= 32;
        }

        return Arrays.toString(ans);
    }
    
    public static String dashatize(int num) {
        StringBuilder ans = new StringBuilder();
        String number = Integer.toString(num);
        for (int i = 0; i < number.length(); i++) {
            if (Integer.parseInt(String.valueOf(number.charAt(i))) % 2 == 0) ans.append(number.charAt(i));
            else ans.append("-").append(number.charAt(i)).append("-");
        }
        return ans.toString();
    }
    
//    public static String lcs(String x, String y) {
//        String[] substrX = new String[] {};
//        for (int i = 0; i < x.length(); i++) {
//            for (int j = i+1; j <= x.length(); j++) {
//                String[] tempArr = new String[]
//            }
//        }
//        return "";
//    }
    
    public static String binaryToText(String binary) {
        if (binary.equals("")) return "";
        StringBuilder ans = new StringBuilder();
        String[] binaryArr = binary.split("(?<=\\G........)");
        for (String i : binaryArr) ans.append((char) Integer.parseInt(i, 2));
        return ans.toString();
    }
    
    
    public static void main(String[] args) {
        //System.out.println(Solution.validatePin("11111ws"));
        //System.out.println(Solution.toCamelCase("the-Stealth-Warrior"));
        //System.out.println(Solution.driver(new String[]{"Johanna", "",       "Gibbs", "13-Dec-1981",       "F"}));
        //System.out.println(Solution.solution(10));
        //System.out.println(Solution.camelCase("to camel case"));
        //System.out.println(Solution.dashatize(223));
        System.out.println(Solution.binaryToText("0100100001100101011011000110110001101111"));
    }

}