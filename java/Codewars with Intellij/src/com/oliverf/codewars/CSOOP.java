package com.oliverf.codewars;

import java.util.Random;
import java.util.Scanner;

public class CSOOP {

    protected int numOfRepeats;
    
    public CSOOP(int amountOfRepeats) {
        numOfRepeats = amountOfRepeats;
    }
    
    public void playGame(int lowestNum, int highestNum) {
        Random rand = new Random();
        int secretNum = rand.nextInt(highestNum-lowestNum) + lowestNum + 1;
        for (int i = 0; i < numOfRepeats; i++) {
            Scanner sc = new Scanner(System.in);
            System.out.println("Input a number between " + lowestNum + " and " + highestNum + ": ");
            int userInput = sc.nextInt();
            if (userInput > secretNum)
                System.out.println("Too high!");
            else if (userInput < secretNum)
                System.out.println("Too low!");
            else if (userInput == secretNum) {
                System.out.println("Correct!");
                break;
            } else
                System.out.println("Invalid input.");
        }
    }
    
    public static void main(String[] args) {
        CSOOP g1 = new CSOOP(7);
        g1.playGame(1, 100);
    }

}
