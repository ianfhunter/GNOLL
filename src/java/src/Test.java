import org.gnoll.DiceNotationParser;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;
import java.io.IOException;

public class Test {
    public static void main(String[] args) {
        String fn = "tmp.dice";
        File myObj = new File(fn); 
        myObj.delete();
        int r = DiceNotationParser.roll("1d200",fn);

        System.out.println("GNOLL RC:"+r);
        assert r == 0;
        
        Path path = Paths.get(fn);
        List<String> lines;
        try{
            lines = Files.readAllLines(path);
        }
        catch(IOException e) {
            lines = Collections.<String>emptyList();
            assert false;
        }
        System.out.println("GNOLL Rolled:" + lines.get(0));

    }
}
