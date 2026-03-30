//use std::ffi::CStr;
use std::process;
use std::fs::File;
use std::io::{self, BufRead};

extern "C" {
    pub fn gnoll_validate_roll_request(die: *const cty::c_char) -> cty::c_int;
    pub fn roll_and_write(
        die: *mut cty::c_char,
        fp: *mut cty::c_char
    ) -> cty::c_int;
}

fn main() {

    println!("Example of GNOLL in rust...\n");
    
    let die = "10d20\0".as_ptr() as *mut cty::c_char;
    let fp = "output.txt\0".as_ptr() as *mut cty::c_char;
    
    unsafe {
        let v = gnoll_validate_roll_request(die as *const _);
        if v != 0 {
            eprintln!("GNOLL validate error: {}", v);
            process::exit(1);
        }
        let rc = roll_and_write(die, fp);
        if rc != 0 {
            eprintln!("GNOLL roll error: {}", rc);
            process::exit(1);
        }

        // Read the result from the memory pointed to by fp
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
                let cleaned_string = result_str.replace(";", "");
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
