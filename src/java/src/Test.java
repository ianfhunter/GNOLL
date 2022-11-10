import org.gnoll.DiceNotationParser;
public class Test {
    public static void main(String[] args) {
        String fn = "tmp.dice";
        File myObj = new File(fn); 
        myObj.delete()
        int r = DiceNotationParser.roll("1d200",fn);

        System.out.println("GNOLL RC:"+r);
        assert r == 0;
        
        Path path = Paths.get(fn);
        List<String> lines = Files.readAllLines(path);
        System.out.println("GNOLL Rolled:", lines[0]);
    }
}
