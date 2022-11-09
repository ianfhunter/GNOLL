package org.gnoll;

public class DiceNotationParser{
    static { System.loadLibrary("libdice"); }
    public static native int roll(String s);

}

