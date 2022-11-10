package org.gnoll;

public class DiceNotationParser{
    static { System.loadLibrary("dice"); }
    public static native int roll(String s, String fn);

}

