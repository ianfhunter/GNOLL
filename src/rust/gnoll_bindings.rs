use std::ffi::CStr;
use std::process;

extern "C" {
    pub fn roll_and_write(
        die: *mut cty::c_char,
        fp: *mut cty::c_char
    );
}

fn main() {
    let die = "10d20\0".as_ptr() as *mut cty::c_char;
    let fp = "output.txt\0".as_ptr() as *mut cty::c_char;
    
    unsafe { roll_and_write(die, fp) }

    // Read the result from the memory pointed to by fp
    let result_cstr = CStr::from_ptr(fp).expect("Failed fromptr");
    
    if let Ok(result_str) = result_cstr.to_str() {
        if let Ok(result_num) = result_str.parse::<u32>() {
            if result_num > 1 {
                 println!("Result is: {}", result_num);
                 process::exit(0);
            } else {
                println!("Result is not greater than 1");
            }
        } else {
            println!("Failed to parse the result as an integer");
        }
    } else {
        println!("Failed to convert CStr to str");
    }
    process::exit(1);

}
