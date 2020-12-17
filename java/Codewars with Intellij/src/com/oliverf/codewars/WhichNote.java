package com.oliverf.codewars;

public class WhichNote {
    public static String whichNote(int keyPressCount) {
        switch (keyPressCount % 88 % 12) {
            case 0: return "G#";
            case 1: return "A";
            case 2: return "A#";
            case 3: return "B";
            case 4: return "C";
            case 5: return "C#";
            case 6: return "D";
            case 7: return "D#";
            case 8: return "E";
            case 9: return "F";
            case 10: return "F#";
            case 11: return "G";
        }
        return "";
    }
    
    public static void main(String[] args) {
        System.out.println(WhichNote.whichNote(1));
    }
}
