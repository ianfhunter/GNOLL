#[repr(C)]

extern "C" {
    pub fn roll_and_wrie(
        die: *cty::c_char,
        fp: *cty::c_char
    );
}
