package com.oliverf.codewars;

import org.jetbrains.annotations.NotNull;

import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;

public class EncodingWithOllie {
    public static @NotNull String decode(@NotNull String decodeStr) {
        int rot = Integer.parseInt(decodeStr.substring(decodeStr.indexOf("!!!---!!!")+9));
        StringBuilder ans = new StringBuilder();
        int counter = 0;
        for (char i : decodeStr.substring(2, decodeStr.indexOf("!!!---!!!")).toCharArray()) {
            if (counter % 3 == 0)
                ans.append((char) (i - rot % 100));
            counter ++;
        }
        return ans.toString();
    }
    
    public static @NotNull String encode(@NotNull String encodeStr, int rot) {
        
        StringBuilder ans = new StringBuilder();
        for (char i : encodeStr.toCharArray()) {
                ans.append((char) (i + rot % 100));
                for (int j = 0; j < 2; j++) { ans.append(randomChar()); }
        }
        return Character.toString(randomChar()) + randomChar() + ans.toString() + "!!!---!!!" + rot;
    }
    
    public static char randomChar() { return (char) ThreadLocalRandom.current().nextInt(33, 126 + 1); }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Encode or Decode (E or D): ");
        String encDec = sc.nextLine();
        
        if (encDec.toUpperCase().equals("E")) {
            System.out.print("Input what you wish to encode: ");
            String encodeStr = sc.nextLine();
            int rot = ThreadLocalRandom.current().nextInt(1, 26 + 1);
            System.out.println(encode(encodeStr, rot));
        } else if (encDec.toUpperCase().equals("D")) {
            System.out.print("Input what you wish to decode: ");
            String decodeStr = sc.nextLine();
            System.out.println(decode(decodeStr));
        } else { System.out.println("Ya Goofed!"); }
    }
}
