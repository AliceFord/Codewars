package com.oliverf.codewars;

public class Encryption {

    public static String basicEncrypt(String input, int shift) {
        StringBuilder ans = new StringBuilder();
        for (char character : input.toCharArray()) {
            character += shift;
            if ((character > 90 && character < 97 )|| character > 122) character -= 26;
            ans.append(character);
        }
        return ans.toString();
    }

    public static String basicDecrypt(String input, int shift) {
        StringBuilder ans = new StringBuilder();
        for (char character : input.toCharArray()) {
            character -= shift;
            if (character < 65 || (character < 97 && character > 90)) character += 26;
            ans.append(character);
        }
        return ans.toString();
    }

    public static String publicPrivateEncrypt(String input, String publicKey) {


        return "";
    }



    public static void main(String[] args) {
        String test = basicEncrypt("hello", 3);
        System.out.println(test);

        test = basicDecrypt(test, 3);
        System.out.println(test);
    }
}
