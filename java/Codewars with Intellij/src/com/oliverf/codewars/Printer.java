package com.oliverf.codewars;

public class Printer {

    public static String printerError(String s) {
        String ans = "";
        int num = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) > 109) {
                num += 1;
            }
        }
        ans += num;
        if (ans.equals("")) { ans += "0"; }
        ans += "/" + s.length();
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(Printer.printerError("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"));
    }
}
