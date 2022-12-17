#[repr(C)]

extern "C" {
    pub fn roll_and_write(
        die: *cty::c_char,
        fp: *cty::c_char
    );
}

fn main() {
    unsafe { roll_and_write("10d20") }
    println!("Hello, world!");
}
