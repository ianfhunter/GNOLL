
using System
using System.IO

[DllImport ("libdice.so")]
private static extern int roll_and_write (char * string, char * filepath);

 
private static void RollWithGNOLL ()
{
    string roll = "1d20"
    string fn = "output.dice"

    // Delete if exist
    if(File.Exists(fn)){
        File.Delete(fn);
    }

    // Create
    roll_and_write(roll, fn);

    // Read
    using (StreamReader sr = File.OpenText(fn))
    {
        string s;
        while ((s = sr.ReadLine()) != null)
        {
            Console.WriteLine(s);
        }
    }
}


class Example
{
    public static void Main()
    {
        RollWithGNOLL("1d20");
    }
}