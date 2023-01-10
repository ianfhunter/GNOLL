
using System;
using System.IO;
using System.Runtime.InteropServices;
using System.Diagnostics;

[DllImport ("libdice.so", CharSet = CharSet.Ansi)]
static extern int roll_and_write (
    [MarshalAs(UnmanagedType.LPStr)] string dice_string, 
    [MarshalAs(UnmanagedType.LPStr)] string filepath
);
 
static void RollWithGNOLL (string roll_request)
{
    string roll = roll_request;
    string fn = "output.dice";

    // Delete if exist
    if(File.Exists(fn)){
        File.Delete(fn);
    }

    // Create
    int err_code = roll_and_write(roll, fn);

    Debug.Assert(err_code == 0, "GNOLL errored. Check error code");

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

RollWithGNOLL("1d20");
