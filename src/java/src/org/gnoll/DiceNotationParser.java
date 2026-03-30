package org.gnoll;

public class DiceNotationParser{
    static { System.loadLibrary("dice"); }
    public static native int roll(String s, String fn);

    /** Pre-parse bounds check (same as C {@code gnoll_validate_roll_request}). */
    public static native int validateRollRequest(String notation);

}

