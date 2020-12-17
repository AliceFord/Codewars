package com.oliverf.codewars;

import java.util.Map;
import java.util.HashMap;

class ParseMolecule {
    
    public static Map<String,Integer> getAtoms(String formula) {
        Map<String, Integer> ans = new HashMap<String, Integer>();
        
        formula += "````";
        
        for (int i = 0; i < formula.length(); i++) {
            if (!(formula.charAt(i) == '(' || formula.charAt(i) == ')' || formula.charAt(i) == '[' || formula.charAt(i) == ']' || formula.charAt(i) == '{' || formula.charAt(i) == '}')) {
                if (formula.charAt(i) >= 65 && formula.charAt(i) <= 90) {
                    if (formula.charAt(i) >= 97 && formula.charAt(i) <= 122) {
                        //ans.
                    }
                }
            }
        }
        
        return ans;
    }
}