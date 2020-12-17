package com.oliverf.codewars;

public class HumanReadableTime {
    public static String makeReadable(int seconds) {
        int hours, minutes;
        hours = seconds / 3600; seconds %= 3600;
        minutes = seconds / 60; seconds %= 60;
        return String.format("%02d", hours) + ":" + String.format("%02d", minutes) + ":" + String.format("%02d", seconds);
    }
    
    public static void main(String[] args) {
        System.out.println(HumanReadableTime.makeReadable(3600));
    }
}