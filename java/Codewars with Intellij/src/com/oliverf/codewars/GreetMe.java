package com.oliverf.codewars;

public class GreetMe{
    public static String greet(String name){
        String ans = "";
        name = name.toLowerCase();
        char ansT = name.charAt(0);
        ans = ans.toUpperCase() + name.substring(1) + "!";
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(GreetMe.greet("teSa"));
    }
}