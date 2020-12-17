package com.oliverf.codewars;

class Biker {
    public static int temps(double v0, double slope, double dTot) {
        final double GRAVITY_ACC = 9.81 * 3.6 * 60.0;                        // gravity acceleration
        final double DRAG        = 60.0 * 0.3 / 3.6;                         // force applied by air on the cyclist
        final double DELTA_T     = 1.0 / 60.0;                               // in minutes
        final double G_THRUST    = 60 * 3.6 * 3.6;                           // pedaling thrust
        final double MASS        = 80.0;                                     // biker's mass
        final double WATTS0      = 225.0;                                    // initial biker's power
        final double D_WATTS     = 0.5;
        
        
        double slopeGrav = GRAVITY_ACC * Math.atan(slope/100);
        System.out.println(slopeGrav);
        return -1;
    }
    
    public static void main(String[] args) {
        System.out.println(temps(30, 5, 30));
    }
}