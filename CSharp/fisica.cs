using System;

public class Eletroestatica {
    public static void Main(int[] args) {
        F = 4 * 10**-3 N
        r = 9 * 10**-2 m
        F = k * (q1 * q2) r**2
        q1 = q2
        4 * 10**-3 N = (9 * 10**9 N m**2/C**2) * (q1 * q2) / (0.09 m)**2
        4 * 10**-3 N = (9 * 10**9 N m**2/C**2) * (q1 * q2) / 0.0081 m**2
        4 * 10**-3 N = 1.11 * 10**12 N m**2/C**2 * (q1 * q2)
        4 * 10**-3 N = 1.11 * 10**12 N m**2/C**2 * (q**2 * (-1))
        q**2 = -4 * 10**-3 N / (1.11 * 10**12 N m**2/C**2 * (-1))
        q**2 = -3.6 * 10**-15 C**2
        |q| = √(-3.6 * 10**-15 C**2)
        **|q| = 6 ** 10**-8 C**
        6 * 10**-8 
    }
}