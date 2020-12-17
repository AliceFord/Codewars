package com.oliverf.codewars;

public class RoboScript {
    
    public static String highlight(String code) {
        String charType = "", newCharType = "";
        StringBuilder ans = new StringBuilder();
        for (char i : code.toCharArray()) {
            newCharType = Character.toString(i);
            try {
                Integer.parseInt(Character.toString(i));
                newCharType = "0";
            } catch (Exception ignored) {}
            if (newCharType.equals(charType) && !newCharType.equals(")") && !newCharType.equals("(")) {
                ans.insert(ans.lastIndexOf("<"), i);
            } else {
                switch (newCharType) {
                    case "F":
                        ans.append("<span style=\"color: pink\">F</span>");
                        break;
                    case "L":
                        ans.append("<span style=\"color: red\">L</span>");
                        break;
                    case "R":
                        ans.append("<span style=\"color: green\">R</span>");
                        break;
                    case "0":
                        ans.append("<span style=\"color: orange\">").append(i).append("</span>");
                        break;
                    case "(":
                        ans.append("(");
                        break;
                    case ")":
                        ans.append(")");
                        break;
                }
            }
            charType = newCharType;
            
        }
        return ans.toString();
    }
    
    public static void main(String[] args) {
        System.out.println(RoboScript.highlight("(2902))41)712906)L039RLL48)4784542L1F"));
    }
    
}