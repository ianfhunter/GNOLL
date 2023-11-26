use std::ffi::CStr;
use std::process;

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
        let result_cstr = CStr::from_ptr(fp);
    
        if let Ok(result_str) = result_cstr.to_str() {
            if let Ok(result_num) = result_str.parse::<u32>() {
                if result_num > 1 {
                    println!("Result is: {}\n", result_num);
                    process::exit(0);
                } else {
                    println!("Result is not greater than 1\n");
                }
            } else {
                println!("Failed to parse the result as an integer\n");
            }
        } else {
            println!("Failed to convert CStr to str\n");
        }
    }
    println!("Fatal.\n");
    process::exit(1);

}
