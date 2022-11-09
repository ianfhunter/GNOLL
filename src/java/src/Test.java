import org.gnoll.DiceNotationParser;
public class Test {
    public static void main(String[] args) {
        int r = DiceNotationParser.roll("1d200");

        System.out.println("GNOLL RC:"+r);
    }
}
