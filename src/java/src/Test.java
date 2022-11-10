import org.gnoll.DiceNotationParser;
import java.nio.file.*;
import java.util.*;
import java.io.*;

public class Test {
    public static void main(String[] args) {
        String fn = "tmp.dice";
        Path fp = Paths.get(fn);
        File f =  new File(fn);

        f.delete();
        try{
            f.createNewFile();
        }
        catch(IOException e) {
            assert false;
        }
        
        int gnoll_return_code = DiceNotationParser.roll("1d200", fn);
        // System.out.println("GNOLL RC:"+r);
        assert gnoll_return_code == 0;

        try{
            List<String> lines = Files.readAllLines(fp);
            assert lines.size() > 0 ;
            System.out.println("GNOLL Rolled:" + lines.get(0));
        }
        catch(IOException e) {
            assert false;
        }
    }
}
