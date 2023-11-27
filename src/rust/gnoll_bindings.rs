//use std::ffi::CStr;
use std::process;
use std::fs::File;
use std::io::{self, BufRead};

extern "C" {
    pub fn roll_and_write(
        die: *mut cty::c_char,
        fp: *mut cty::c_char
    );
}

fn main() {

    println!("Example of GNOLL in rust...\n");
    
    let die = "10d20\0".as_ptr() as *mut cty::c_char;
    let fp = "output.txt\0".as_ptr() as *mut cty::c_char;
    
    unsafe { roll_and_write(die, fp) }

    // Read the result from the memory pointed to by fp
    unsafe { 
        //let result_cstr = CStr::from_ptr(fp);
        let file_path = "output.txt";
        let file = File::open(file_path).unwrap();
        let reader = io::BufReader::new(file);

       // Read the first line
        if let Some(Ok(first_line)) = reader.lines().next() {
            // Use the first line as needed
            let result_cstr = std::ffi::CString::new(first_line).unwrap();
            // Rest of your code...
        
            if let Ok(result_str) = result_cstr.to_str() {
                let cleaned_string = original_string.replace(";", "");
                if let Ok(result_num) = cleaned_string.parse::<u32>() {
                    if result_num > 1 {
                        println!("Result is: {}\n", result_num);
                        process::exit(0);
                    } else {
                        println!("Result is not greater than 1\n");
                    }
                } else {
                    println!("Failed to parse the result '{}' as an integer\n", cleaned_string);
                }
            } else {
                println!("Failed to convert CStr to str\n");
            }
        }
    }
    println!("Fatal.\n");
    process::exit(1);

}
